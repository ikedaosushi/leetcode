func twoSum(nums []int, target int) []int {
    answer := []int{}
    main:
    for i, num1 := range nums {
        for j, num2 := range nums {
            if i == j {
                continue
            }
            tmp_target := num1 + num2
            if target == tmp_target {
                answer = []int{i, j}
                break main
            }
        }
    }
    return answer
}