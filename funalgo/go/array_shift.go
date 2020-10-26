package main

import "fmt"

func main() {
	var arr_r = []int{1,2,3,4,5}
	RightShift(arr_r, 3)
	fmt.Println(arr_r)
}

func RightShift(arr []int, delta int)  {
	reverse(arr[delta:])
	reverse(arr[:delta])
	reverse(arr[:])
}

func reverse(arr []int) {
	for i, j := 0, len(arr) - 1; i < j; i, j = i + 1, j - 1 {  //i < len(arr) && j >= 0
		arr[i], arr[j] = arr[j], arr[i]
	}
}