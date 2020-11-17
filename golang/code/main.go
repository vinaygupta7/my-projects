package main

import (
	"fmt"

	"github.com/vinaygupta7/mywebservices/models"
)

func main() {
	fmt.Println("hello my main module")
	u := models.User{
		ID:        2,
		FirstName: "Arvind",
		LastName:  "Gupta",
	}
	fmt.Println(u)
}
