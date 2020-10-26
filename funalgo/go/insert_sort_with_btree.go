package main

import (
	"fmt"
)


//二叉树(排序树)实现插入排序
type tree struct {
	value int
	left, right *tree
}

func main() {
	var arr = []int{4,2,1,3}
	Sort(arr)
	fmt.Println(arr)
	//append(arr[:0], 1)

	//slc小实验
	var slc1 = make([]int, 5, 10)
	_ = append(slc1[:3], 1,2)
	_ = append(slc1[:3], 3,4)
	fmt.Println(slc1, len(slc1))

	slc1 = make([]int, 5, 10)
	_ = append(slc1[:0], 1, 2)
	fmt.Println(slc1)
	_ = append(slc1[:2], 3, 4)
	fmt.Println(slc1)

	fmt.Println("头插测试")
	var slc2 = make([]int, 10, 20)
	var slc_temp = slc2[:0]
	for i := 0; i < 10; i++ {
		slc_temp = append(slc_temp, i * i)
		fmt.Println(slc2)
	}
}


func Sort(values []int) {
	var root *tree
	for i, val := range values {
		fmt.Println("current:", i, val)
		root = add(root, val)  //和add的赋值是一样的作用，看起来有些奇怪
	}
	appendValues(values[:0], root)
	//return appendValues(values[:0], root)
}

func add(t *tree, val int) *tree {
	if t == nil {
		t = new(tree)
		t.value = val
		return t
		//node := tree{
		//	value: val,
		//}
		//return &node
	}
	//这里赋值看起来有些奇怪。。实际上是个小技巧，主要是考虑到需要为nil孩子创建新节点的情况
	if t.value < val {
		t.right = add(t.right, val)
	} else {
		t.left = add(t.left, val)
	}
	return t
}

func appendValues(values []int, t *tree) []int {
	if t != nil {
		values = appendValues(values, t.left)
		values = append(values, t.value)
		values = appendValues(values, t.right)
	}
	return values
}