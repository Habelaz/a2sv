class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # memo = {}
        s = sum(nums)
        if s % 2 != 0:
            return False
        halfSum = s // 2

        @cache

        def part(i,summ):
            nonlocal halfSum
            if i >= len(nums):
                return summ == halfSum

            return part(i+1,summ) or part(i+1,summ + nums[i])
        
        return part(0,0)

        
            
