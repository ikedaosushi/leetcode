func searchLeftIndex(nums []int, target int) int {
	low, high := 0, len(nums)
	for low < high {
		mid := int((low + high) / 2)
		if target < nums[mid] || target == nums[mid] {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}

func searchRightIndex(nums []int, target int) int {
	low, high := 0, len(nums)
	for low < high {
		mid := int((low + high) / 2)
		if target < nums[mid] {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return high
}

func searchRange(nums []int, target int) []int {
	leftIndex := searchLeftIndex(nums, target)
	if len(nums) <= leftIndex || nums[leftIndex] != target {
		return []int{-1, -1}
	}
	rightIndex := searchRightIndex(nums, target) - 1
	return []int{leftIndex, rightIndex}
}