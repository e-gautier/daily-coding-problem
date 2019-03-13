package main

/*
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
*/

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	pi := 3.141
	succeed := 3

	t1 := approximatePi(1, 10000000)
	if t1 != pi {
		fmt.Printf("t1 failed, expected %f got %f \n", pi, t1)
		succeed--
	}
	t2 := approximatePi(2, 10000000)
	if t2 != pi {
		fmt.Printf("t2 failed, expected %f got %f \n", pi, t2)
		succeed--
	}
	t3 := approximatePi(3, 10000000)
	if t3 != pi {
		fmt.Printf("t3 failed, expected %f got %f \n", pi, t3)
		succeed--
	}

	fmt.Printf("success: %d/%d \n", succeed, 3)
}

func pointInCircle(r int, x float64, y float64) int {
	if math.Pow(x, 2)+math.Pow(y, 2) <= math.Pow(float64(r), 2) {
		return 1
	}
	return 0
}

func approximatePi(r int, totalRandomPoint int) float64 {
	pointsInsideTheCircle := 0
	for i := 0; i < totalRandomPoint; i++ {
		x := rand.Float64() * float64(r)
		y := rand.Float64() * float64(r)
		pointsInsideTheCircle = pointsInsideTheCircle + pointInCircle(r, x, y)
	}
	return math.Round((float64(pointsInsideTheCircle)/float64(totalRandomPoint))*4*1000) / 1000
}
