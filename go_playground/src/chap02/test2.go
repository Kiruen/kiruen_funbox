package main

import (
	"container/list"
	"fmt"
	"strconv"
	"strings"
)

const (
Sunday int = iota
Monday
Tuesday
	)

const (
	FLAG_1 int = 1 << iota
	FLAG_2
	FLAG_3
	FLAG_4
)

const (
	_ = 1 << (10 * iota)
	KB
	MB
	GB
	TB
	PB
)

func main() {
	var li list.List
	li.PushFront(1)
	li.PushBack(2)
	fmt.Println(li)

	var a, b = 7, 1 << 1
	fmt.Println(a &^ b)

	var n1 int16 = 12
	var n2 int = 12
	//var n2 int8
	//var num int16 = n2 + n1
	fmt.Println(n1, n2)
	fmt.Printf("%d %[1]o %#[1]o\n", 0666)
	fmt.Println(comma_right(12314123))
	fmt.Println([]byte("ASfa"))

	fmt.Println(strings.Split(comma_right(12314123), ",")[2])

	var sb strings.Builder
	sb.WriteRune('せ')  //UTF-8字符
	sb.WriteString("abc")
	sb.WriteByte(65)
	fmt.Println(sb.String())

	fmt.Printf("%b\n", 12)
	fmt.Println(strconv.ParseInt("2131234", 10, 64))

	const (
	 pi float32 = 3.14
	 e = 2.71
	 t string = ""
	)
	fmt.Println(float64(pi))
	fmt.Println(Sunday, Tuesday)
	fmt.Println(FLAG_1 | FLAG_2 | FLAG_3)
	fmt.Println(PB)

	var symbols = [...]string{10:"AAA"}
	fmt.Println(symbols, len(symbols), cap(symbols))

	fmt.Println([...]int{1,2,3} == [3]int{1,2,3})
	//fmt.Println([...]int{1,2,3} == [4]int{1,2,3})

	arr := [32]int{1}
	zero(&arr)
	fmt.Println(arr)


	var num_ int
	var str_ string
	nInputStrs, _ := fmt.Scanf("%d,%s", &num_, &str_)
	fmt.Println(nInputStrs, num_, str_)
}

func zero(ptr *[32]int) {
	for i := range ptr {
		ptr[i] = 0
	}
}

func comma_right(num int) string {
	str := strconv.Itoa(num)
	var res = ""
	var i int
	for i = len(str); i - 3 > 0 ; i -= 3 {
		res = "," +  str[i-3:i] + res
	}
	return str[:i] + res
}

func comma_wrong(num int) string {
	str := strconv.Itoa(num)
	var sb strings.Builder
	var i int
	for i = 0; i + 3 < len(str); i += 3 {
		sb.WriteString(str[i:i+3])
		sb.WriteString(",")
	}
	sb.WriteString(str[i:])
	return sb.String()
	//for ch := range str {
	//	fmt.Println(ch)
	//}
}