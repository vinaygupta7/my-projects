package main

import (
	"fmt"
)

func main() {

	const pi = 3.1415
	fmt.Println(pi)
	//Error when assign value to constant
	//pi = 1.2

	const c = 3
	fmt.Println(c + 3)
	fmt.Println(float32(c) + 1.2)

}
