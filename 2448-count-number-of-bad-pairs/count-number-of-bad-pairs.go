func countBadPairs(nums []int) int64 {
    badPairs := 0
    count := make(map[int]int)

    for i := 0; i < len(nums); i++ {
        diff := i - nums[i]
        badPairs += i - count[diff]
        count[diff] += 1
    }
    return int64(badPairs)
}