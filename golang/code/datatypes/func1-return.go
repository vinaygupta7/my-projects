package main

import (
	"fmt"
)

func main() {
	port := 3000
	isStarted := startWeb(port)
	fmt.Println(isStarted)

}

func startWeb(ports int) bool {

	fmt.Println("Starting Web Server ...")
	fmt.Println("WebServer Started on Port!", ports)
	return true
}
