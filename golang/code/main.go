package main

import (
	"net/http"

	"github.com/vinaygupta7/mywebservices/controllers"
)

func main() {
	//fmt.Println("hello my main module")
	//u := models.User{
	//	ID:        2,
	//	FirstName: "Arvind",
	//	LastName:  "Gupta",
	//}
	controllers.RegisterControllers()
	http.ListenAndServe(":3000", nil)
	//fmt.Println(u)
}
