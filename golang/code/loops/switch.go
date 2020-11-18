package main

type HTTPRequest struct {
	Method string
}

func main() {
	r := HTTPRequest{Method: "HEAD"}

	switch r.Method {
	case "GET":
		println("GET REQUEST")
		fallthrough
	case "DELETE":
		println("DELETE REQUEST")
		//fallthrough
	case "POST":
		println("POST REQUEST")
	case "PUT":
		println("PUT REQUEST")
	default:
		println("Unhandled METHOD")
	}
}
