package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	const MAX = 1000000
	results := map[int]int{1: 0}
	bestSeed := 0
	maxRes := 0

	for i := MAX; i >= 1; i-- {
		seed := i
		len := 0
		for {
			if rest, ok := results[seed]; ok {
				len += rest
				//fmt.Println("calc", i, "stop at", seed)
				if len > maxRes {
					bestSeed = i
					maxRes = len
				}
				results[i] = len
				break
			}

			if seed%2 == 0 {
				seed /= 2
			} else {
				seed = seed*3 + 1
			}
			len += 1
		}
	}
	fmt.Println(bestSeed, maxRes)
	fmt.Println("time:", time.Now().Sub(now).Seconds())
}
