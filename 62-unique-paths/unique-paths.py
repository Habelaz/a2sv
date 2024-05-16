class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # @cache
        # def dp(i,j):
        #     if i >= m or j >= n:
        #         return 0
        #     if i == m-1 and j == n-1:
        #         return 1

        #     return dp(i+1,j) + dp(i,j+1)

        # return dp(0,0)

        dp = [[0 for i in range(n)] for j in range(m)]

        dp[-1][-1] = 1

        def inbound(i,j):
            if 0 <=i < m and 0 <= j < n:
                return dp[i][j]
            return 0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] += inbound(i+1,j) + inbound(i,j+1)

        return dp[0][0]