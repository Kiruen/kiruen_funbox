package mylib

import "fmt"

var names []string

func Hello(name string) {
	fmt.Printf("Hello, %s\n", name)
}

func get_float(val float64) float64 {
	//var a = true float64(a)
	return 3 / 2 + val
}

func Get_local() *int {
	var v = 1
	return &v
}

type Number int
func (n Number) BeautifulString() string {
	return fmt.Sprintf("<%d>", n)
}

func Fib(n int) int {
	//x, y := 1, 1
	//for i := 2; i <= n; i++ {
	//	x, y = y, x + y
	//}
	x, y := 0, 1
	for i := 0; i < n; i++ {
		x, y = y, x + y
	}
	return x
}

func Gcd(x, y int) int  { //func gcd(x int, y int)
	for y != 0 {
		//想象把竹尖砍去拿下来，然后和之前的短竹交换下位置，进行下一轮
		//大的总会被换到左边，不用关心x y的大小
		x, y = y, x % y
	}
	return x
}