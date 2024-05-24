class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        dp = [[0] * n for _ in range(n)] 
        dp[-1] = matrix[-1]
        def inbound(i,j):
            if 0 <= i < n and 0 <= j < n:
                return dp[i][j]
            return float('inf')
        for i in range(n-2,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = min(inbound(i+1,j-1),inbound(i+1,j),inbound(i+1,j+1)) + matrix[i][j]
        return min(dp[0])

        

