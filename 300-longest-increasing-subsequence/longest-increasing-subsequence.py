class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # @cache
        # def dp(i,prev):
        #     if i >= len(nums):
        #         return 0
        #     if nums[i] > prev:
        #         return max(dp(i+1,nums[i])+1,dp(i+1,prev))
        #     return dp(i+1,prev)

        # return dp(0,float('-inf'))
        n = len(nums)
        @cache
        def dp(i):
            if i >= n:
                return 0
            ans = 1
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    ans = max(ans,dp(j) + 1)
            return ans

        return max([dp(i) for i in range(n)])

        
