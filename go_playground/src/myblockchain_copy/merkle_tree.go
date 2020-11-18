package main

import (
	"crypto/sha256"
)

// MerkleTree represent a Merkle tree
type MerkleTree struct {
	RootNode *MerkleNode
}

// MerkleNode represent a Merkle tree node
type MerkleNode struct {
	Left  *MerkleNode
	Right *MerkleNode
	Data  []byte
}

// NewMerkleTree creates a new Merkle tree from a sequence of data
func NewMerkleTree(data [][]byte) *MerkleTree {
	var nodes []MerkleNode
	//补全偶数个数据
	if len(data)%2 != 0 {
		data = append(data, data[len(data)-1])
	}

	//为每个data创建一个叶节点
	for _, datum := range data {
		node := NewMerkleNode(nil, nil, datum)
		nodes = append(nodes, *node)
	}
	//叶节点的一半数量，即上层非叶节点的数量
	for i := 0; i < len(data)/2; i++ {
		var newLevel []MerkleNode
		//每两个节点搞出一个新非叶节点，
		for j := 0; j < len(nodes); j += 2 {
			node := NewMerkleNode(&nodes[j], &nodes[j+1], nil)
			newLevel = append(newLevel, *node)
		}
		//本层构造完毕，交给下层去接着构造
		nodes = newLevel
	}
	//最后只取第一个节点，即root，把它交上去
	mTree := MerkleTree{&nodes[0]}

	return &mTree
}

// NewMerkleNode creates a new Merkle tree node
func NewMerkleNode(left, right *MerkleNode, data []byte) *MerkleNode {
	mNode := MerkleNode{}
	//没有子树了，直接hash数据
	if left == nil && right == nil {
		hash := sha256.Sum256(data)
		mNode.Data = hash[:]
	} else {
		//否则，左右子树的数据黏到一起进行一次hash
		//☆这里不会改变left.Data的底层数组的内容吗？(虽然切片的表现不受影响)
		prevHashes := append(left.Data, right.Data...)
		hash := sha256.Sum256(prevHashes)
		mNode.Data = hash[:]
	}

	mNode.Left = left
	mNode.Right = right

	return &mNode
}
