func search(nums []int, target int) int {
	n := len(nums)
	var low, high int
	high = n - 1

	// Find lowest index
	for low < high {
		mid := int((low + high) / 2)
		// fmt.Println(nums[high], nums[mid])
		if nums[high] < nums[mid] {
			low = mid + 1
		} else {
			high = mid
		}
	}
	// fmt.Println("found lowest index")
	// fmt.Println(n, low, high)

	root := low
	low, high = 0, n-1

	for low <= high {
		mid := int((low + high) / 2)
		realmid := (root + mid) % n
		if nums[realmid] == target {
			return realmid
		} else if nums[realmid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	// fmt.Println(n, low, high, root)

	return -1
}