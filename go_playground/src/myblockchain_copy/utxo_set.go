package main

import (
	"encoding/hex"
	"log"

	"github.com/boltdb/bolt"
)

const keystr_utxoBucket = "chainstate"

// UTXOSet represents UTXO set
type UTXOSet struct {
	Blockchain *Blockchain
}

// FindSpendableOutputs finds and returns unspent outputs to reference in inputs
//根据pubkeyHash寻找它所拥有的可花费outputs，找够amount为止
func (u UTXOSet) FindSpendableOutputs(pubkeyHash []byte, amount int) (int, map[string][]int) {
	unspentOutputs := make(map[string][]int)
	accumulated := 0
	db := u.Blockchain.db

	err := db.View(func(tx *bolt.Tx) error {
		b_utxo := tx.Bucket([]byte(keystr_utxoBucket))
		c := b_utxo.Cursor()

		//k v都是[]byte。遍历未花费交易 局部的每笔交易，
		for k, v := c.First(); k != nil; k, v = c.Next() {
			txID := hex.EncodeToString(k)  //key是交易id。搞成字符串，便于放到map中
			outs := DeserializeOutputs(v)  //value是outputs数组。
			//挨个检查交易的每个输出
			for outIdx, out := range outs.Outputs {
				//如果该UTXO指向的是我(用公钥hash比较)，就可以花这个输出了
				//如果还没攒够目标钱数，就继续扫描outputs（别忘了，超出的钱可以找零哦）
				if out.IsLockedWithKey(pubkeyHash) && accumulated < amount {
					accumulated += out.Value
					//记录下该输出，通过交易 ID 进行分组
					unspentOutputs[txID] = append(unspentOutputs[txID], outIdx)
				}
			}
		}

		return nil
	})
	if err != nil {
		log.Panic(err)
	}

	return accumulated, unspentOutputs
}

// FindUTXO finds UTXO for a public key hash
func (u UTXOSet) FindUTXO(pubKeyHash []byte) []TXOutput {
	var UTXOs []TXOutput
	db := u.Blockchain.db

	err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(keystr_utxoBucket))
		c := b.Cursor()

		for k, v := c.First(); k != nil; k, v = c.Next() {
			outs := DeserializeOutputs(v)

			for _, out := range outs.Outputs {
				if out.IsLockedWithKey(pubKeyHash) {
					UTXOs = append(UTXOs, out)
				}
			}
		}

		return nil
	})
	if err != nil {
		log.Panic(err)
	}

	return UTXOs
}

// CountTransactions returns the number of transactions in the UTXO set
func (u UTXOSet) CountTransactions() int {
	db := u.Blockchain.db
	counter := 0

	err := db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(keystr_utxoBucket))
		c := b.Cursor()

		for k, _ := c.First(); k != nil; k, _ = c.Next() {
			counter++
		}

		return nil
	})
	if err != nil {
		log.Panic(err)
	}

	return counter
}

// Reindex rebuilds the UTXO set
//重新保存UTXO集到数据库中
func (u UTXOSet) Reindex() {
	db := u.Blockchain.db
	bucketName := []byte(keystr_utxoBucket)

	err := db.Update(func(tx *bolt.Tx) error {
		//尝试删除数据库中旧的UTXO Set 的bucket
		err := tx.DeleteBucket(bucketName)
		if err != nil && err != bolt.ErrBucketNotFound {
			log.Panic(err)
		}
		//重新创建
		_, err = tx.CreateBucket(bucketName)
		if err != nil {
			log.Panic(err)
		}

		return nil
	})
	if err != nil {
		log.Panic(err)
	}
	//把现有的UTXO集内的东西拽过来
	UTXO := u.Blockchain.FindUTXO()

	err = db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket(bucketName)

		for txID, outs := range UTXO {
			key, err := hex.DecodeString(txID)  //以交易id作为key
			if err != nil {
				log.Panic(err)
			}
			//一个一个地再放到新的bucket中
			err = b.Put(key, outs.Serialize())
			if err != nil {
				log.Panic(err)
			}
		}
		return nil
	})
}

// Update updates the UTXO set with transactions from the Block
// The Block is considered to be the tip of a blockchain
//更新的单位是一个区块
func (u UTXOSet) Update(block *Block) {
	db := u.Blockchain.db

	err := db.Update(func(tx *bolt.Tx) error {
		//注意b是utxo数据表
		b := tx.Bucket([]byte(keystr_utxoBucket))
		//交易-输入-输出
		for _, tx := range block.Transactions {
			if tx.IsCoinbase() == false {
				for _, vin := range tx.Vin {
					updatedOuts := TXOutputs{}
					//找出该输入依赖的输出所在的交易（同一个交易的vin们引用的交易一般不会重复吧）
					outsBytes := b.Get(vin.Txid)
					outs := DeserializeOutputs(outsBytes)

					for outIdx, out := range outs.Outputs {
						//在引用过去的交易中找vin以外的其他输出，准备放到该引用交易的UTXO子集中
						if outIdx != vin.Vout {
							updatedOuts.Outputs = append(updatedOuts.Outputs, out)
						}
					}
					//如果updated为空，表示它被完全花费了，掏空了，就从UTXO数据表中删除掉该交易的item
					if len(updatedOuts.Outputs) == 0 {
						err := b.Delete(vin.Txid)
						if err != nil {
							log.Panic(err)
						}
					} else {
						//如果没有花完，就把该交易的最新UTXO数组更新一下
						err := b.Put(vin.Txid, updatedOuts.Serialize())
						if err != nil {
							log.Panic(err)
						}
					}

				}
			}
			//这里还把所有交易的输出都认为是该交易未花费的输出。但到下一次迭代的时候很可能就会被改变
			newOutputs := TXOutputs{}
			for _, out := range tx.Vout {
				newOutputs.Outputs = append(newOutputs.Outputs, out)
			}
			//☆那会不会出现一个问题：前面刚被更新过，这里又被覆盖了？
			err := b.Put(tx.ID, newOutputs.Serialize())
			if err != nil {
				log.Panic(err)
			}
		}

		return nil
	})
	if err != nil {
		log.Panic(err)
	}
}
