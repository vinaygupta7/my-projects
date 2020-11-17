package main

import "fmt"

func main() {

	//	arr := [3]int{1, 2, 3}

	//	slice := arr[:]

	//	arr[1] = 42
	//	slice[2] = 70

	//	fmt.Println(arr, slice)

	slice := []int{3, 2, 5}
	fmt.Println(slice)

	slice = append(slice, 4, 3, 56)
	fmt.Println(slice)

	s2 := slice[1:]

	s3 := slice[:2]

	s4 := slice[1:2]

	fmt.Println(s2, s3, s4)
}
