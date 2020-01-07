import (
	"fmt"
	"sort"
)

func longestCommonPrefix(strs []string) string {
	var ret []rune
	// i := 0
	var lens []int
	//
	for _, str := range strs {
		lens = append(lens, len(str))
	}

	sort.Ints(lens)
	if len(lens) == 0 {
		return ""
	}

	min_len := lens[0]
	// fmt.Printf("min_len: %v", min_len)

	for i := 0; i < min_len; i++ {
		var current_rune rune
		isCommon := true
		for idx, str := range strs {
			// fmt.Printf("i: %i, idx: %v, str: %v\n", i, idx, str)
			if idx == 0 {
				current_rune = []rune(str)[i]
			} else {
				if current_rune != []rune(str)[i] {
					isCommon = false
				} else {
					fmt.Printf("same")
				}
			}
		}
		if isCommon {
			ret = append(ret, current_rune)
		} else {
			break
		}
	}

	return string(ret)
}