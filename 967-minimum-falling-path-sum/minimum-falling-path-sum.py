class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def dp(i,j):
            if i >= n:
                return 0
            if j < 0 or j >= n:
                return float('inf')

            return matrix[i][j] + min(dp(i+1,j),dp(i+1,j-1),dp(i+1,j+1))

        return min([dp(0,i) for i in range(n)])

        

