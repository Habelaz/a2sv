class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(n):
            if n == 1:
                return 0

            ans = n
            divisor = 2
            while divisor * divisor <= n:
                if n % divisor == 0:
                    ans = min(ans,dp(n//divisor) + divisor)
                divisor += 1
            return ans
        
        return dp(n)