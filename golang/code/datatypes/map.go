package main

import "fmt"

func main() {

	m := map[string]int{"vinay": 32}
	fmt.Println(m)
	fmt.Println(m["vinay"])

	m["vinay"] = 30
	fmt.Println(m)

	delete(m, "vinay")
	fmt.Println(m)
}
