class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dp = defaultdict(int)
        dp[0] = -1
        target = sum(nums) % p
        curSum = 0
        result = len(nums)
        
        if sum(nums) % p == 0: return 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            
            curMod = curSum % p
            
            temp = (curSum - target) % p
            
            if temp in dp:
                if i - dp[temp] < result:
                    result = i - dp[temp]
            
            dp[curMod] = i
        
        return result if result < len(nums) else -1