package main

import "bytes"

// TXInput represents a transaction input
type TXInput struct {
	Txid      []byte  //☆当然表示其引用回去的交易啦
	Vout      int  //在引用交易的outs中的索引位置
	Signature []byte
	PubKey    []byte
}

// UsesKey checks whether the address initiated the transaction
func (in *TXInput) UsesKey(pubKeyHash []byte) bool {
	lockingHash := HashPubKey(in.PubKey)

	return bytes.Compare(lockingHash, pubKeyHash) == 0
}
