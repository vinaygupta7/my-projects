package main

import (
	"fmt"
)

func main() {
	port := 3000
	//port, err := startWeb(port)
	_, err := startWeb(port)
	//fmt.Println(port, err)
	fmt.Println(err)
}

func startWeb(port int) (int, error) {

	fmt.Println("Starting WebServer")
	//return nil
	//return errors.New("Something went wrong")
	return port, nil
}
