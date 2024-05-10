class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count = 0
        memo = {}
        def dp(i,summ):
            nonlocal count
            if i == len(nums):
                return 1 if target == summ else 0
            if (i,summ) not in memo:
                memo[(i,summ)] = dp(i+1,summ - nums[i]) + dp(i+1,summ + nums[i])
                
    
            return memo[(i,summ)]

        return dp(0,0)