class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        exp_sum= sum(range(0,n+1))
        act_sum=sum(nums)
        return exp_sum - act_sum

        