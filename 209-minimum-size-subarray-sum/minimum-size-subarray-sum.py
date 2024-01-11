class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        ans = float('inf')
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                curr_sum -= nums[l]
                ans = min(ans,r-l+1)
                l += 1
        if ans == float('inf'):
            return 0
        return ans
        