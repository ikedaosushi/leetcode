func isValidSudoku(board [][]byte) bool {
	for i := 0; i < 9; i++ {
		rowNums := []byte{}
		colNums := []byte{}

		for j := 0; j < 9; j++ {
			// row
			rowTarget := board[i][j]
			if rowTarget == '.' {

			} else if !isIn(rowNums, rowTarget) {
				rowNums = append(rowNums, rowTarget)
			} else {
				return false
			}
			// col
			colTarget := board[j][i]
			if colTarget == '.' {

			} else if !isIn(colNums, colTarget) {
				colNums = append(colNums, colTarget)
			} else {
				return false
			}
		}
	}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			start_x := i * 3
			start_y := j * 3
			boxs := []byte{}
			for x := start_x; x < start_x+3; x++ {
				for y := start_y; y < start_y+3; y++ {
					// fmt.Println(x, y)
					boxTarget := board[x][y]
					if boxTarget == '.' {
						continue
					} else if !isIn(boxs, boxTarget) {
						boxs = append(boxs, boxTarget)
					} else {
						return false
					}
				}
			}
		}
	}
	return true
}

func isIn(nums []byte, target byte) bool {
	for _, i := range nums {
		if i == target {
			return true
		}
	}
	return false
}