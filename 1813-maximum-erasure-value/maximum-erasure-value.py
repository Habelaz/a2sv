class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        ans = set()
        max_s = 0
        summ = 0
        for r in range(len(nums)):
            
            while nums[r] in ans:
                ans.remove(nums[l])
                summ -= nums[l]
                l += 1
            ans.add(nums[r])
            summ += nums[r]
            max_s = max(max_s,summ)
        return max_s
