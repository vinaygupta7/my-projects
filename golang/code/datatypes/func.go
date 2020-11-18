package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello, Vinay")
	port := 3000
	startWeb(port, 2)

}

func startWeb(ports int, numberofretries int) {
	//func startWeb(ports, numberofretries int) {

	fmt.Println("Starting Web Server ...")
	fmt.Println("WebServer Started on Port!", ports)

	fmt.Println("No of retries:", numberofretries)
}
