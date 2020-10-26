package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
	"time"
)

func main() {
	var sb = struct {
		age int
	}{age:12}
	fmt.Println(sb)

	fmt.Printf("%#o\n", 066)

	fmt.Println(foo_multi_return())
	fmt.Println(foo_input_int_and_string(foo_multi_return()))
	fmt.Println(foo_input_params(foo_multi_return()))

	var foo func(...int) string
	foo = foo_input_params
	if foo != nil {
		fmt.Println(foo(1,2,3,4))
	}

	fmt.Println(strings.Map(func(r rune) rune {
		r++
		return r
	}, "HAL-9000"))

	var eles = []int{1,2,3,4}
	handle_foreach(eles, func(ints []int, i int) {
		ints[i]++
	})
	fmt.Println(eles)

	do_something_big_and_slow()

	look_into_return_value(20)
	fmt.Println(manip_return_value(20))

	//var op (f Num) func(a Num) Num
	var op func(f Num, a Num) Num
	op = Num.Add
	fmt.Println(op(1, 6))
}

type Num int
func (f Num) Add(a Num) Num {
	return f + a
}

func (f Num) Sub(a Num) Num {
	return f - a
}

func look_into_return_value(x int) (result int)  {
	defer func() { fmt.Println("返回值是：", result) }()
	return x * x
}

func manip_return_value(x int) (result int)  {
	defer func() { result *= 2 }()
	return x * x
}

func do_something_big_and_slow()  {
	defer trace()()
	time.Sleep(2 * time.Second)
}

func trace() func() {
	start := time.Now()
	log.Printf("[%v] Start! \n", start)
	return func() {
		log.Printf("[%v]End. [%v]\n", time.Now(), time.Since(start))
	}
}

func handle_foreach(eles []int, handler func([]int, int)) {
	for i, _ := range eles {
		handler(eles, i)
	}
}

func foo_input_params(args... int) string {
	return fmt.Sprintf("args is a slice(1=True)? %v", interface{}(args).([]int)[0])
}

func foo_input_int_and_string(int, int) string {
	return "OK"
}

func foo_multi_return() (a int, b int) {
	a = 1
	b, _ = strconv.Atoi("123")
	return
}