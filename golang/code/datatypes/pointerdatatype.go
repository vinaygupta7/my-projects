package main

import "fmt"

func main() {
	var firstName *string = new(string)

	//firstName = "Vinay"
	*firstName = "Vinay"

	fmt.Println(firstName)
	fmt.Println(*firstName)

	////////////////////////////////////SAME LOCATION DATA/////////////////////////////////////
	secondName := "Gupta"
	fmt.Println(secondName)

	ptr := &secondName
	fmt.Println(ptr, *ptr)

	secondName = "KAKA"
	fmt.Println(ptr, *ptr)

}
