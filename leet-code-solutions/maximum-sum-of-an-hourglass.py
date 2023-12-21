class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxx = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m-2):
            for j in range(n-2):
                submatrix = [
                grid[i][j:j+3],
                grid[i+1][j:j+3],
                grid[i+2][j:j+3]
                ]
                summ = sum(submatrix[0])
                summ += sum(submatrix[2]) + submatrix[1][1]
                maxx = max(summ,maxx)
        return maxx
            
