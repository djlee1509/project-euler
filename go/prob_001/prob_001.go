package main

import "fmt"

type numbers []int

func numberRange(maxNum int) numbers {
	divisibleNums := numbers{}

	for num := 1; num < maxNum; num++ {
		if (num%3 == 0) || (num%5 == 0) {
			divisibleNums = append(divisibleNums, num)
		}
	}
	return divisibleNums
}

func sum(numList numbers) int {
	total := 0
	for _, v := range numList {
		total += v
	}
	return total
}

func main() {
	numList := numberRange(1000)
	result := sum(numList)
	fmt.Println(result)
}
