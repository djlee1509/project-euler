package main

import "fmt"

type evenNums []int

func fibSeq(maxNum int) evenNums {
	x, y := 1, 2
	evenList := evenNums{}

	for y < maxNum {
		if y%2 == 0 {
			evenList = append(evenList, y)
		}
		x, y = y, x+y
	}
	return evenList
}

func (nl evenNums) total() int {
	total := 0
	for _, v := range nl {
		total += v
	}
	return total
}

func main() {
	fs := fibSeq(100)
	total := fs.total()
	fmt.Println(total)
}
