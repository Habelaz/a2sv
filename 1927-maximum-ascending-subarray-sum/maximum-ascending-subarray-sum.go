func maxAscendingSum(nums []int) int {
    ans := nums[0]
    sum := nums[0]

    for i := 1; i < len(nums); i++ {
        if nums[i] > nums[i-1] {
            sum += nums[i]
            // ans = int(math.Max(float64(ans), float64(sum)))
        }else{
            // ans = int(math.Max(float64(ans), float64(sum)))
            sum = nums[i]
        }
        if sum > ans {
            ans = sum
        }

    }
    return ans
}