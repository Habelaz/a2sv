class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(i,a):
            if i >= len(coins) or a > amount:
                return 0
            
            if a == amount:
                return 1

            return dp(i,coins[i]+a) + dp(i+1,a)
            
        return dp(0,0)