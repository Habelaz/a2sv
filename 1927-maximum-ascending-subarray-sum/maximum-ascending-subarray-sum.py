class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        ans = nums[0]
        summ = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                summ += nums[i]
                ans = max(summ,ans)
            else:
                ans = max(summ,ans)
                summ = nums[i]
        return ans