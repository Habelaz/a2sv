class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_len = float('inf')
        curr_sum = 0

        for right in range(n):
            curr_sum += nums[right]

            # Shrink the window from the left until the sum is less than target
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0
        return min_len