func removeDuplicates(nums []int) int {
    i := 0
    for j := 1; j < len(nums); j ++ {
        if nums[i] != nums[j] {
            i++
            nums[i] = nums[j]
        }
    }
    return i+1
}


// func delete(s []int, i int) []int {
//     s = append(s[:i], s[i+1:]...)
//     return s
// }


// func removeDuplicates(nums []int) int {
//     if len(nums) == 0 {
//         return 0
//     }
//     var currentN int
//     i := 0
//     for {
//         n := nums[i]
//         if i > 0 && n == currentN {
//             nums = delete(nums, i)
//         } else {
//             currentN = n 
//             i++
//         }

//         if i >= len(nums) {
//             break
//         }
//     }
//     return len(nums)
// }

