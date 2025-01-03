class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0 for i in range(len(nums))]
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            prefix[i] = acc
        total = sum(nums)
        ans = 0
        for i in range(len(nums)-1):
            if prefix[i] >= total - prefix[i]:
                ans += 1
        
        return ans