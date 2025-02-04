func isArraySpecial(nums []int) bool {
    for i, v := range nums {
        if i == 0 {
            continue
        }
        if v % 2 == nums[i - 1] % 2 {
            return false
        }
    }
    return true
}