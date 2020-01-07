func romanToInt(s string) int {
	result := 0

	sym2val := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	sym2beforeSym := map[string]string{
		"V": "I", "X": "I",
		"L": "X", "C": "X",
		"D": "C", "M": "C",
	}

	before := ""

	for _, rune_ := range s {
		string_ := string(rune_)
		if beforeSym, ok := sym2beforeSym[string_]; ok && (before == beforeSym) {
			beforeVal := sym2val[before]
			result -= beforeVal * 2
		}
		result += sym2val[string_]
		before = string_
	}
	return result
}