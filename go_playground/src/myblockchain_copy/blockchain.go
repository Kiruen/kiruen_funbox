package main

import (
	"bytes"
	"crypto/ecdsa"
	"encoding/hex"
	"errors"
	"fmt"
	"log"
	"os"

	"github.com/boltdb/bolt"
)

const dbFile = "blockchain_%s.db"
const keystr_blocksBucket = "blocks"
const genesisCoinbaseData = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"

// Blockchain implements interactions with a DB
type Blockchain struct {
	tip []byte
	db  *bolt.DB
}

// CreateBlockchain creates a new blockchain DB
func CreateBlockchain(address, nodeID string) *Blockchain {
	dbFile := fmt.Sprintf(dbFile, nodeID)
	if dbExists(dbFile) {
		fmt.Println("Blockchain already exists.")
		os.Exit(1)
	}

	var tip []byte

	//coinbase交易的输出给了这个address
	cbtx := NewCoinbaseTX(address, genesisCoinbaseData)
	genesis := NewGenesisBlock(cbtx)

	db, err := bolt.Open(dbFile, 0600, nil)
	if err != nil {
		log.Panic(err)
	}

	//创建一个区块链，首先要创建一个创世区块
	err = db.Update(func(tx *bolt.Tx) error {
		//为该区块链创建一个bucket
		b, err := tx.CreateBucket([]byte(keystr_blocksBucket))
		if err != nil {
			log.Panic(err)
		}
		//向bucket放入创世区块
		err = b.Put(genesis.Hash, genesis.Serialize())
		if err != nil {
			log.Panic(err)
		}

		err = b.Put([]byte("l"), genesis.Hash)
		if err != nil {
			log.Panic(err)
		}
		tip = genesis.Hash

		return nil
	})
	if err != nil {
		log.Panic(err)
	}
	//创世区块创建完毕，构造区块链对象
	bc := Blockchain{tip, db}

	return &bc
}

// NewBlockchain creates a new Blockchain with genesis Block
//事实上只是从文件恢复区块链实体对象，并不是重新创建一个区块链
func NewBlockchain(nodeID string) *Blockchain {
	dbFile := fmt.Sprintf(dbFile, nodeID)
	if dbExists(dbFile) == false {
		fmt.Println("No existing blockchain found. Create one first.")
		os.Exit(1)
	}

	var tip []byte
	db, err := bolt.Open(dbFile, 0600, nil)
	if err != nil {
		log.Panic(err)
	}

	err = db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(keystr_blocksBucket))  //尝试获取blocks，不存在就创建
		tip = b.Get([]byte("l"))  //l对应最后一个区块的hash

		return nil
	})
	if err != nil {
		log.Panic(err)
	}

	bc := Blockchain{tip, db}  //还存一个bucket连接实例

	return &bc
}

// AddBlock saves the block into the blockchain
func (bc *Blockchain) AddBlock(block *Block) {
	err := bc.db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(keystr_blocksBucket))
		blockInDb := b.Get(block.Hash)  //尝试获取block每个区块的hash就是key

		if blockInDb != nil {
			return nil
		}

		blockData := block.Serialize()
		err := b.Put(block.Hash, blockData)
		if err != nil {
			log.Panic(err)
		}

		lastHash := b.Get([]byte("l"))
		lastBlockData := b.Get(lastHash)
		lastBlock := DeserializeBlock(lastBlockData)

		//判断是否确实是在他后面（☆物理上的后面，这里>其实应该是 == .. + 1？）
		if block.Height > lastBlock.Height {
			err = b.Put([]byte("l"), block.Hash)
			if err != nil {
				log.Panic(err)
			}
			bc.tip = block.Hash
		}

		return nil
	})
	if err != nil {
		log.Panic(err)
	}
}

// FindTransaction finds a transaction by its ID
func (bc *Blockchain) FindTransaction(ID []byte) (Transaction, error) {
	bci := bc.Iterator()

	for {
		block := bci.Next()

		for _, tx := range block.Transactions {
			if bytes.Compare(tx.ID, ID) == 0 {
				return *tx, nil
			}
		}

		if len(block.PrevBlockHash) == 0 {
			break
		}
	}

	return Transaction{}, errors.New("Transaction is not found")
}

// FindUTXO finds all unspent transaction outputs and returns transactions with spent outputs removed
//在数据库中找UTXO，收集他们，返回UTXO集（其实是一个map）
func (bc *Blockchain) FindUTXO() map[string]TXOutputs {
	UTXOsOfTx := make(map[string]TXOutputs)
	//临时存放所有已花费的交易输出，string是交易ID——每个交易都有一个容器int[]存放STXOs
	spentTXOs := make(map[string][]int)
	bci := bc.Iterator()

	for {
		//来到一个区块
		block := bci.Next()

		//遍历所有交易，收集所有的UTXO
		for _, tx := range block.Transactions {
			txID := hex.EncodeToString(tx.ID)

		Outputs:
			//遍历交易的所有输出...
			for outIdx, out := range tx.Vout {
				// Was the output spent?
				//看spentTXOs有没有此交易。若找到了，说明它也有
				if spentTXOs[txID] != nil {
					for _, spentOutIdx := range spentTXOs[txID] {
						//如果outIdx出现在已花费的交易输出当中（☆这里是不是用个set更好一点？）
						if spentOutIdx == outIdx {
							continue Outputs  //直接跳到下一个交易
						}
					}
				}
				//txID没有出现在已花费交易输出当中，表明它是个UTXO，我们向该交易对应的UTXO集中记录这个tx
				outs := UTXOsOfTx[txID]  //这里只是取出一个还没填充数据的结构体
				outs.Outputs = append(outs.Outputs, out)
				UTXOsOfTx[txID] = outs
			}
			//如果不是coinbase交易，那就顺便：把该交易的 全部输入对应回去的交易 标记为已花费
			if tx.IsCoinbase() == false {
				for _, in := range tx.Vin {
					inTxID := hex.EncodeToString(in.Txid)
					spentTXOs[inTxID] = append(spentTXOs[inTxID], in.Vout)
				}
			}
		}
		//数据库遍历结束
		if len(block.PrevBlockHash) == 0 {
			break
		}
	}

	return UTXOsOfTx
}

// Iterator returns a BlockchainIterat
func (bc *Blockchain) Iterator() *BlockchainIterator {
	bci := &BlockchainIterator{bc.tip, bc.db}

	return bci
}

// GetBestHeight returns the height of the latest block
//返回链的最大高度，就是最后一个区块的高度呗
func (bc *Blockchain) GetBestHeight() int {
	var lastBlock Block

	err := bc.db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(keystr_blocksBucket))
		lastHash := b.Get([]byte("l"))
		blockData := b.Get(lastHash)
		lastBlock = *DeserializeBlock(blockData)

		return nil
	})
	if err != nil {
		log.Panic(err)
	}

	return lastBlock.Height
}

// GetBlock finds a block by its hash and returns it
func (bc *Blockchain) GetBlock(blockHash []byte) (Block, error) {
	var block Block

	err := bc.db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(keystr_blocksBucket))

		blockData := b.Get(blockHash)

		if blockData == nil {
			return errors.New("Block is not found.")
		}

		block = *DeserializeBlock(blockData)

		return nil
	})
	if err != nil {
		return block, err
	}

	return block, nil
}

// GetBlockHashes returns a list of hashes of all the blocks in the chain
func (bc *Blockchain) GetBlockHashes() [][]byte {
	var blocks [][]byte
	bci := bc.Iterator()

	for {
		block := bci.Next()

		blocks = append(blocks, block.Hash)

		if len(block.PrevBlockHash) == 0 {
			break
		}
	}

	return blocks
}

// MineBlock mines a new block with the provided transactions
//打包/创建新区块/挖矿，准备交易数据并调用POW算法
func (bc *Blockchain) MineBlock(transactions []*Transaction) *Block {
	var lastBlockHash []byte
	var lastHeight int

	for _, tx := range transactions {
		// TODO: ignore transaction if it's not valid
		//把收集的交易都拽出来验证一下，看看答案是不是都正确（就是执行脚本的过程）
		if bc.VerifyTransaction(tx) != true {
			log.Panic("ERROR: Invalid transaction")
		}
	}

	err := bc.db.View(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(keystr_blocksBucket))
		lastBlockHash = b.Get([]byte("l"))

		blockData := b.Get(lastBlockHash)
		block := DeserializeBlock(blockData)

		lastHeight = block.Height

		return nil
	})
	if err != nil {
		log.Panic(err)
	}

	//创建新的区块，实际上就包含了POW的过程
	newBlock := NewBlock(transactions, lastBlockHash, lastHeight+1)

	err = bc.db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(keystr_blocksBucket))
		err := b.Put(newBlock.Hash, newBlock.Serialize())
		if err != nil {
			log.Panic(err)
		}

		err = b.Put([]byte("l"), newBlock.Hash)
		if err != nil {
			log.Panic(err)
		}

		bc.tip = newBlock.Hash

		return nil
	})
	if err != nil {
		log.Panic(err)
	}

	return newBlock
}

// SignTransaction signs inputs of a Transaction
//跟verifyTransaction一样，也是先收集引用的交易，然后再进行真正的验证
func (bc *Blockchain) SignTransaction(tx *Transaction, privKey ecdsa.PrivateKey) {
	prevTXs := make(map[string]Transaction)

	for _, vin := range tx.Vin {
		prevTX, err := bc.FindTransaction(vin.Txid)
		if err != nil {
			log.Panic(err)
		}
		prevTXs[hex.EncodeToString(prevTX.ID)] = prevTX
	}

	tx.Sign(privKey, prevTXs)
}

// VerifyTransaction verifies transaction input signatures
//对该交易进行验证。注意和(tx *Transaction) Verify是依赖关系
func (bc *Blockchain) VerifyTransaction(tx *Transaction) bool {
	if tx.IsCoinbase() {
		return true
	}

	prevTXs := make(map[string]Transaction)
	//收集交易的每个输入引用的交易，加入到prevTXs(引用交易集)中
	for _, vin := range tx.Vin {
		prevTX, err := bc.FindTransaction(vin.Txid)
		if err != nil {
			log.Panic(err)
		}
		prevTXs[hex.EncodeToString(prevTX.ID)] = prevTX
	}
	//收集好了所有输出至此的交易，一起交给tx进行验证
	return tx.Verify(prevTXs)
}

func dbExists(dbFile string) bool {
	if _, err := os.Stat(dbFile); os.IsNotExist(err) {
		return false
	}

	return true
}
