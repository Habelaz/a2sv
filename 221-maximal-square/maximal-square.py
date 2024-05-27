class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols = len(matrix) , len(matrix[0])
        dp = [[0] * (cols+1) for _ in range(rows + 1)]
        side_length = 0

        for r in range(rows):
            for c in range(cols):

                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c+1],dp[r+1][c],dp[r][c]) + 1
                
                side_length = max(side_length,dp[r+1][c+1])
        
        return side_length * side_length