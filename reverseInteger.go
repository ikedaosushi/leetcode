import "strconv"

func reverse(x int) int {

	isMinus := false
	if x < 0 {
		isMinus = true
		x = x * -1
	}

	a := strconv.Itoa(x)

	n := 0

	rune := make([]rune, len(a))
	for _, r := range a {
		rune[n] = r
		n++
	}

	rune = rune[0:n]

	for i := 0; i < n/2; i++ {
		rune[i], rune[n-1-i] = rune[n-1-i], rune[i]
	}

	b := string(rune)
	// fmt.Printf("%v\n", b)
	// c, _ := strconv.Atoi(b)
	c, err := strconv.ParseInt(b, 10, 32)

	if err != nil {
		return 0
	}
	// fmt.Printf("%v\n", err)

	if isMinus {
		c = c * -1
	}

	return int(c)
}
