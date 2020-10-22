
package main

import (
	"chap02/mylib"
	"flag"
	"fmt"
	. "os"
	"regexp"
)


var name string
var cmdLine = flag.NewFlagSet("question", flag.ExitOnError)

func init() {
	//flag.StringVar(&name, "name", "Someone", "Hello")
	//flag.Usage = func() {
	//	fmt.Println("自己琢磨吧")
	//	flag.PrintDefaults()
	//}
	//flag.CommandLine = flag.NewFlagSet("", flag.ExitOnError)
	//flag.CommandLine.Usage = func() {
	//	fmt.Println("自己琢磨吧")
	//	flag.PrintDefaults()
	//}
	cmdLine = flag.NewFlagSet("", flag.ExitOnError)
	cmdLine.Usage = func() {
		fmt.Println("自己琢磨吧")
		cmdLine.PrintDefaults()
	}
	cmdLine.StringVar(&name, "name", "Someone", "Hello")
}

func parse_cmd()  {
	//flag.Parse()
	cmdLine.Parse(Args[1:])
	mylib.Hello(name)

	res := regexp.MustCompile(`(\w+) \\1`)
	fmt.Println(res.FindAllString("asd sd fas fas aaa bbb bbb", -1))
}

var block string = "outer"
func main() {
	var f, err = Open("test.txt")
	fmt.Println(f, err)
	f, err = Create("test1.log")

	var a, b int = 1, 2
	a, b = b, a
	fmt.Println(a, b)

	var pstr *string = nil
	fmt.Println(pstr == nil)
	var str = "old"
	pstr = &str
	*pstr = "new"
	fmt.Println(str)

	fmt.Println(*mylib.Get_local())

	str_ := new(string)
	fmt.Println(str_, *str_ == "")

	type Blob struct { }
	fmt.Println(new(Blob), new(struct{}))

	fmt.Println(mylib.Fib(5))
	fmt.Println(mylib.Gcd(512, 36), mylib.Gcd(36, 512))
	//var res = str_.(int)

	var li = []string{"a", "ab", "abc"}
	li[2] = "ABC"
	fmt.Printf("%v\n", li)
	fmt.Println(([]byte)("sadasd"))
	var num mylib.Number = 1
	fmt.Println(num.BeautifulString())

	var q = 1
	n1, q := 2, 3
	fmt.Println(a, q, n1)
	block := 444444
	fmt.Println("block=", block)
	container := []string{"a", "b"}
	fmt.Println("ctn[1]=", container[1])
	{
		block := 1.24
		fmt.Println("block=", block)
		container := map[int]string{1:"a", 2:"b"}
		fmt.Println("ctn[1]=", container[1])
	}
	foo()


	val, ok := interface{}(block).(string)
	fmt.Println(ok, val)


	emptySlice := []string{}
	emptyMap := map[string][]string{}
	emptyArray := [3]string{}

	emptySlice = append(emptySlice, "blob")
	emptyMap["ky"] = emptySlice
	emptyArray[2] = "asfji"
	fmt.Println(emptySlice, emptyMap, emptyArray)


	slice0 := make([]int, 5, 8)
	fmt.Println(len(slice0), cap(slice0))

	fmt.Println(slice0[:cap(slice0)])
	fmt.Println(slice0[:len(slice0)])
	//fmt.Println(slice0[:100])

	arr := [5]int{1,2,3,4,5}
	slice1 := arr[:3]
	fmt.Println(arr, slice1)
	slice1 = append(slice1, 1)
	fmt.Println(arr, slice1)
}

func foo() {
	fmt.Println("block=", block)
}