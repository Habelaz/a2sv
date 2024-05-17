class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]

        dp[-1][-1] = 1

        def inbound(i,j):
            if 0 <=i < m and 0 <= j < n and obstacleGrid[i][j] != 1:
                return dp[i][j]
            return 0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] += inbound(i+1,j) + inbound(i,j+1)

        return dp[0][0]