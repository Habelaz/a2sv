class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if len(coins) == 1 and coins[0] < amount:
        #     return -1
        @cache
        def dp(diff):
            if diff == 0:
                return 0
            ans = float('inf')
            for c in coins:
                if diff - c >= 0:
                    curr = dp(diff - c) + 1
                    ans = min(ans,curr)
            return ans
        minn = dp(amount)
        return -1 if minn == float('inf') else minn