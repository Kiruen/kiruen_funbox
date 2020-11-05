package myblock

import (
	"github.com/boltdb/bolt"
)

type Block struct {
	Timestamp     int64
	Data          []byte
	PrevBlockHash []byte
	Hash          []byte
	Nonce         int
}

type Blockchain struct {
	//Blocks []*Block
	tip []byte
	db *bolt.DB
}

func (bc *Blockchain) AddBlock(data string) {
	prevBlock := bc.Blocks[len(bc.Blocks)-1]
	newBlock := NewBlock(data, prevBlock.Hash)
	bc.Blocks = append(bc.Blocks, newBlock)

}

//func (b *Block) SetHash() {
//  有点不太理解为什么Timestamp要先变成字符串然后字符串再变bytes。干嘛不直接int64变bytes？
//  是不是因为无所谓？反正只是个标识，用字符串也一样，而却字符串转bytes要简便一些
//	timestamp := []byte(strconv.FormatInt(b.Timestamp, 10))
//	headers := bytes.Join([][]byte{b.PrevBlockHash, b.Data, timestamp}, []byte{})  //[]byte{}是Hash的占位
//	hash := sha256.Sum256(headers)
//
//	b.Hash = hash[:]
//}

//func NewBlock(data string, prevBlockHash []byte) *Block {
//	//block := &Block{time.Now().Unix(), []byte(data), prevBlockHash, []byte{}}
//	//block.SetHash()
//	//return block
//
//	block := &Block{time.Now().Unix(), []byte(data), prevBlockHash, []byte{}, 0}
//	//fmt.Println(block.Timestamp, strconv.FormatInt(block.Timestamp, 10))
//	pow := NewProofOfWork(block)  //看，newblock的时候已经创建过一次了
//	nonce, hash := pow.Run()
//	block.Hash = hash[:]
//	block.Nonce = nonce
//
//	return block
//}

func NewBlockchain() *Blockchain {
	var tip []byte
	db, _ := bolt.Open(dbFile, 0600, nil)

	_ = db.Update(func(tx *bolt.Tx) error {
		b := tx.Bucket([]byte(blocksBucket))

		if b == nil {
			genesis := NewGenesisBlock()
			b, _ := tx.CreateBucket([]byte(blocksBucket))
			_ = b.Put(genesis.Hash, genesis.Serialize())
			_ = b.Put([]byte("l"), genesis.Hash)
			tip = genesis.Hash
		} else {
			tip = b.Get([]byte("l"))
		}

		return nil
	})

	bc := Blockchain{tip, db}

	return &bc
}

func NewGenesisBlock() *Block {
	return NewBlock("Genesis Block", []byte{})
}

func NewBlockchain() *Blockchain {
	return &Blockchain{[]*Block{NewGenesisBlock()}}
}
