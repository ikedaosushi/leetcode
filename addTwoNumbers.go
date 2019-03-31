import "math/big"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	firstVal := new(big.Int)
	digit := 0
	currentNode := l1
	for {
		a := big.NewInt(int64(currentNode.Val))
		b := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(digit)), nil)
		tmpVal := new(big.Int).Mul(a, b)
		firstVal = new(big.Int).Add(firstVal, tmpVal)
		digit++
		currentNode = currentNode.Next
		if currentNode == nil {
			break
		}
	}
	secondVal := new(big.Int)
	currentNode = l2
	digit = 0
	for {
		a := big.NewInt(int64(currentNode.Val))
		b := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(digit)), nil)
		tmpVal := new(big.Int).Mul(a, b)
		secondVal = new(big.Int).Add(secondVal, tmpVal)
		digit++
		currentNode = currentNode.Next
		if currentNode == nil {
			break
		}
	}
	sum := new(big.Int).Add(firstVal, secondVal)

	if sum.Cmp(big.NewInt(0)) == 0 {
		return &ListNode{}
	}

	returnNode := ListNode{}
	currentNode = nil
	digit = 0
	newVal := new(big.Int)
	for {
		newVal = new(big.Int).Div(sum, new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(digit)), nil))
		// newVal = new(big.Int).Div(sum, big.NewInt(int64(math.Pow(10, float64(digit)))))
		// fmt.Printf("newVal: %v\n", newVal)
		if digit > 1000 {
			break
		}
		if newVal.Cmp(big.NewInt(0)) == 0 {
			currentNode.Next = nil
			break
		} else {
			if currentNode == nil {
				currentNode = &returnNode
			} else {
				currentNode.Next = &ListNode{}
				currentNode = currentNode.Next
			}

			tmp := new(big.Int).Mod(newVal, big.NewInt(int64(10)))
			// fmt.Printf("%v\n", int(tmp.Int64()))
			currentNode.Val = int(tmp.Int64())

			digit++
		}
	}

	return &returnNode
}