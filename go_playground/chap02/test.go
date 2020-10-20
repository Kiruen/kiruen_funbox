package main

import (
	"fmt"
	"regexp"
)

func main() {
	res := regexp.MustCompile(`(\w+) \\1`)
	fmt.Println(res.FindAllString("asd sd fas fas aaa bbb bbb", -1))
}