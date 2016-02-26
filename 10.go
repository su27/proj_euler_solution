package main

import (
	"fmt"
	"math"
)

func main() {
	const max = 2000000
	sqrt := int(math.Floor(math.Sqrt(max)))
	numbers := make([]int, max)
	for i, _ := range numbers {
		numbers[i] = i
	}

	factor := make([]int, sqrt)
	numbers[1] = 0
	for i, _ := range factor[2:] {
		if i < 2 || numbers[i] == 0 {
			continue
		}
		for bad := i * 2; bad < max; bad += i {
			numbers[bad] = 0
		}
	}

	sum := 0
	for _, i := range numbers {
		sum += i
	}
	fmt.Println(sum)
}
