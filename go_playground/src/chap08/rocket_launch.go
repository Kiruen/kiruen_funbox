package main

import (
	"fmt"
	"os"
	"time"
)

func launcher1()  {
	var timeCh = time.Tick(1 * time.Second)
	var abortCh = make(chan struct{})
	go func() {
		os.Stdin.Read(make([]byte, 1))
		abortCh<- struct{}{}
	}()
	for i := 10; i >= 0; i-- {
		select {
		case <-abortCh:
			fmt.Println("Program aborted")
			return
		case <-timeCh:
			fmt.Println(i)
		}
	}
}

func launcher2() {
	var abortCh = make(chan struct{})
	go func() {
		os.Stdin.Read(make([]byte, 1))
		abortCh<- struct{}{}
	}()
	select {
	case <-time.After(10 * time.Second):
		fmt.Println("Go!")
	case <-abortCh:
		fmt.Println("Aborted!")
	}
}

func boringGame()  {
	//ch := make(chan int)
	//ch := make(chan int, 3)
	ch := make(chan int, 1)
	for i := 0; i < 10; i++ {
		select {
		case ch<- i:
		case j := <-ch:
			fmt.Println(j)
		}
	}
}

func main() {
	launcher1()
}