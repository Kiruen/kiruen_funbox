package main

import (
	"fmt"
	"sync"
)

type Counter struct {
	sync.Mutex
	Count int
}

func (c *Counter) Add()  {
	c.Lock()
	c.Count++
	//fmt.Println(c.Count)
	c.Unlock()
}

func main() {
	var counter Counter
	//var counter *Counter = new(Counter)
	var grp sync.WaitGroup
	grp.Add(10)

	for i := 0; i < 10; i++ {
		go func() {
			//counter.Lock()
			defer grp.Done()
			//defer mu.Unlock()
			for j := 0; j < 100000; j++ {
				counter.Add()
			}
		}()
	}
	grp.Wait()
	fmt.Println(counter.Count)
}