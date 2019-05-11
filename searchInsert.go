func searchInsert(nums []int, target int) int {
	low, high := 0, len(nums)
	for low < high {
		mid := int((low + high) / 2)
		if nums[mid] >= target {
			high = mid
		} else {
			low = mid + 1
		}
	}

	return low
}