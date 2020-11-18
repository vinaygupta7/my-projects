package main

func main() {
	slice := []int{1, 2, 3}
	for i, v := range slice {
		println(i, v)
	}

	wellknownports := map[string]int{"http": 80, "https": 443}
	for k, j := range wellknownports {
		println(k, ":", j)
	}

	for _, m := range wellknownports {
		println(m)
	}
}
