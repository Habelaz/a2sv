func check(nums []int) bool {
    count := 0
    if nums[len(nums)-1] > nums[0] {
        count += 1
    }
    for i := 1; i < len(nums); i++ {
        if nums[i] < nums[i-1] {
            count += 1
        }
    }
    if count > 1 {
        return false
    }else{
        return true
    }
}