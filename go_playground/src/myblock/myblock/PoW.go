package myblock

import (
	"bytes"
	"crypto/sha256"
	"fmt"
	"math"
	"math/big"
	"strconv"
)

const targetBits = 24  //问题的难度，表示需要前多少位为0

type ProofOfWork struct {
	block  *Block
	target *big.Int
}

//生成一个新的POW器
func NewProofOfWork(b *Block) *ProofOfWork {
	target := big.NewInt(1)
	target.Lsh(target, uint(256 - targetBits))

	pow := &ProofOfWork{b, target}

	return pow
}

func IntToHex(val int64) []byte { //size必须int
	//fmts := "%0" + strconv.Itoa(size) + "X"//%#输出0X1234
	//fmt.Println(strconv.FormatInt(val, 16))
	//fmt.Println("bytes:", []byte(strconv.FormatInt(val, 16)))
	//把val转换成16进制字符串(不带0x前缀)，然后把字符串变成ascii码存到[]byte中
	return []byte(strconv.FormatInt(val, 16))
	 //strings.Split(fmt.Sprintf(fmts, val))
}

func (pow *ProofOfWork) prepareData(nonce int) []byte {
	data := bytes.Join(
		//不规则的byte数组阵：每一行是一个byte数组
		[][]byte{
			pow.block.PrevBlockHash,
			pow.block.Data,
			IntToHex(pow.block.Timestamp),
			IntToHex(int64(targetBits)),
			IntToHex(int64(nonce)),
		},
		[]byte{},
	)

	return data
}

func (pow *ProofOfWork) Validate() bool {
	var hashInt big.Int

	data := pow.prepareData(pow.block.Nonce)
	hash := sha256.Sum256(data)
	hashInt.SetBytes(hash[:])

	isValid := hashInt.Cmp(pow.target) == -1

	return isValid
}

func (pow *ProofOfWork) Run() (int, []byte) {
	var maxNonce = math.MaxInt64
	var hashInt big.Int
	var hash [32]byte
	nonce := 0

	fmt.Printf("Mining the block containing \"%s\"\n", pow.block.Data)
	for nonce < maxNonce {
		data := pow.prepareData(nonce)
		hash = sha256.Sum256(data)
		hashInt.SetBytes(hash[:])

		if hashInt.Cmp(pow.target) == -1 {
			fmt.Printf("\r%x\n", hash)
			break
		} else {
			nonce++
		}
	}
	fmt.Print("\n\n")

	return nonce, hash[:]
}