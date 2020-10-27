package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	step2Ch := make(chan int)
	out := make(chan int)
	go func() {
		for i := 0 ; i < 1000 ; i++ {
			step2Ch <- i
		}
		close(step2Ch)
	}()
	for i := 0 ; i < 100 ; i++ {
		go func() {
			for n := range step2Ch {
				out <- n * n
				time.Sleep(time.Duration(rand.Intn(500)) * time.Millisecond)
			}
			close(out)
		}()
	}
	for sq := range out {
		fmt.Println(sq)
	}
}