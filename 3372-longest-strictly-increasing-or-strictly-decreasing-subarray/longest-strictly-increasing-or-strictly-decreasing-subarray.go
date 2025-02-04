func longestMonotonicSubarray(nums []int) int {
    if len(nums) == 1 {
        return 1
    }
    inc := 1
    dec := 1
    ans := 0
    for i := 1 ; i < len(nums); i++ {
        if nums[i] > nums[i-1] {
            inc += 1
            dec = 1
        } else if nums[i] < nums[i-1] {
            dec += 1
            inc = 1
        } else{
            inc,dec = 1,1
        }
        maxx := (math.Max(float64(dec),float64(inc)))
        ans = int(math.Max(float64(ans),maxx))
    }
    return ans
}
