import (
	"fmt"
	"math"
)

func divideTwoIntegers(dividend int, divisor int) int {

	var positive bool
	x := dividend < 0
	y := divisor < 0

	if (x || y) && !(x && y) {
		positive = false
	} else {
		positive = true
	}
	dividend = int(math.Abs(float64(dividend)))
	divisor = int(math.Abs(float64(divisor)))

	result := 0

	for divisor <= dividend {
		tmp := divisor
		i := 1
		for tmp <= dividend {
			fmt.Printf("[start] tmp: %v, i: %v, dividend: %v \n", tmp, i, dividend)
			dividend -= tmp
			result += i
			tmp <<= 1
			i <<= 1
			fmt.Printf("[ end ] tmp: %v, i: %v, dividend: %v \n", tmp, i, dividend)
		}
	}

	if !positive {
		result = -1 * result
	}

	return int(math.Min(float64(result), 2147483647.))
}