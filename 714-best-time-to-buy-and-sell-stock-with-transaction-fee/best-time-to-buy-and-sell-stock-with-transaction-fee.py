class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dp(i,buying):
            if i >= len(prices):
                return 0

            if (i,buying) not in memo:
                if buying:
                    memo[(i,buying)] = max(dp(i+1,not buying ) - prices[i],dp(i+1,buying))
                else:
                    memo[(i,buying)] = max(dp(i+1,not buying ) + prices[i] - fee,dp(i+1,buying))

            return memo[(i,buying)]

        return dp(0,True) 
               