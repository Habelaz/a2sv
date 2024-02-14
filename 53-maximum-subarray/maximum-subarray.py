class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        maxx = -10000
        for i in range(0,len(nums)):
            curr_max += nums[i]
            if(curr_max<nums[i]):
                curr_max=nums[i]
            if(maxx<curr_max):
                maxx=curr_max
        return maxx
        

        