package main

import (
	"fmt"
	"strings"
)

func intersect1(a []int, b []int) []int {
	m := make(map[int]int)
	for _, num:= range a {  //_, 不能少哦
		m[num]++
	}
	k := 0
	for _, num:= range b {
		if m[num] > 0 {
			m[num] -=1
			b[k] = num
			k++
		}
	}
	return b[:k]
}

//func getLongestPrefixOld(strs []string) string {
	//	raw_pivot, pivot := strs[0], strs[0]
	//	longest_prefix := ""
	//	for k := 1; k < len(raw_pivot); k++{
	//retry:	pivot = raw_pivot[:k]
	//		for _, str := range strs[1:] {
	//			if strings.Index(str, pivot) == -1 {
	//				continue retry
	//			}
	//		}
	//		longest_prefix = pivot
	//	}
	//	return longest_prefix
//}

func getLongestPrefix(strs []string) string {
	pivot := strs[0]
	for _, str := range strs[1:] {
		for strings.Index(str, pivot) == -1 {
			if len(pivot) == 0 {
				return ""
			}
			pivot = pivot[:len(pivot)-1]
		}
	}
	return pivot
}

//a b 有序的版本
func intersect2(a []int, b []int) []int {
	i, j, k := 0, 0, 0
	for i < len(a) && j < len(b) {
		if a[i] == b[j] {
			a[k] = a[i]
			i++;j++;k++
		} else if a[i] < b[j] {
			i++
		} else {
			j++
		}
	}
	return a[:k]
}

func twoSum(nums []int, target int) []int {
	result := []int{}
	m := make(map[int]int)
	for i,k := range nums {
	  if value,exist := m[target-k];exist {
			result = append(result,value)
			result = append(result,i)
		  }
	  m[k] = i
	}
	return result
}

func main() {
	fmt.Println(intersect1([]int{1,2,3,3,3,3,3}, []int{2,3,3,4}))
	fmt.Println(intersect2([]int{1,2,3,3,3,3,3,5}, []int{2,3,3,4,5}))
	fmt.Println(getLongestPrefix([]string{"fat", "fatter", "father", "fats"}))
	fmt.Println(twoSum([]int{1,2,3,4}, 5))
}