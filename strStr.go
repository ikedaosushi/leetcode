func strStr(haystack string, needle string) int {
	if needle == "" {
		return 0
	}
	haystackRunes := []rune(haystack)
	haystackIndex := 0
	needleRunes := []rune(needle)
	needleIndex := 0
	output := 0

	for haystackIndex < len(haystackRunes) {
		// fmt.Println(haystackIndex)
		if haystackRunes[haystackIndex] == needleRunes[needleIndex] {
			if needleIndex == 0 {
				output = haystackIndex
			}
			needleIndex++
			haystackIndex++
			if len(needleRunes) == needleIndex {
				return output
			}
		} else {
			if needleIndex == 0 {
				haystackIndex++
			} else {
				haystackIndex = output + 1
				needleIndex = 0
			}
		}
	}

	return -1
}