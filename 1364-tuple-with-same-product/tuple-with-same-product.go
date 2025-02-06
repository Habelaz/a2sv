func tupleSameProduct(nums []int) int {
    ans := 0
    count := make(map[int]int)

    for i := 0 ; i < len(nums); i++ {
        for j:= 0 ; j < i ; j++  {
            product := nums[i] * nums[j]
            ans += count[product] * 8
            count[product] += 1
            
        }

    } 
    return ans
}