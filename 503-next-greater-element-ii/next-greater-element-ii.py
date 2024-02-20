class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n
        for i in range(2*n):
            while stack and stack[-1][0] < nums[i%n]:
                x = stack.pop()
                a,b = x
                ans[b] = nums[i%n]
            stack.append([nums[i%n],i%n])

        return ans