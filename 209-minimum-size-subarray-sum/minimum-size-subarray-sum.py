class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len=n+1
        l = 0
        curr_sum = 0

        for r in range(n):
            curr_sum += nums[r]

            while curr_sum >= target:
                min_len = min(min_len, r-l+1)
                curr_sum -= nums[l]
                l += 1
        if min_len == n+1:
            return 0
        return min_len