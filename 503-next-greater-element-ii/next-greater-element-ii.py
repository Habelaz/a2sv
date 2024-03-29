class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                x = stack.pop()
                # a,b = x
                ans[x] = nums[i%n]
            stack.append(i%n)

        return ans