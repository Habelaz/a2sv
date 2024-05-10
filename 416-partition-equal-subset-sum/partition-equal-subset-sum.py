class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        memo = {}
        s = sum(nums)
        if s % 2 != 0:
            return False
        halfSum = s // 2

        def ispartition(i,summ):
            nonlocal halfSum
            if i >= len(nums):
                return summ == halfSum

            if (i, summ) not in memo:
                memo[(i, summ)] = ispartition(i+1,summ) or ispartition(i+1,summ + nums[i])

            return memo[(i, summ)]
        
        return ispartition(0,0)

        
            
