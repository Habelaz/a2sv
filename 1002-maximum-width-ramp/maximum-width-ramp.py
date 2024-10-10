class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        ans = 0
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                ind = stack.pop()
                ans = max(ans, i - ind)

        return ans