package main

import "fmt"

func main() {

	type user struct {
		ID        int
		firstName string
		lastName  string
	}
	var u user
	fmt.Println(u)
	u.ID = 1
	u.firstName = "Vinay"
	u.lastName = "Gupta"
	fmt.Println(u)
	fmt.Println(u.firstName)

	u2 := user{ID: 2,
		firstName: "Pooja",
		lastName:  "Gupta", //need to put comma as go appends semicolon End of statement
	}
	fmt.Println(u2)

}
