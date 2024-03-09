class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows[i] = max(rows[i],grid[i][j])
                cols[j] = max(cols[j],grid[i][j])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(rows[i],cols[j]) - grid[i][j]
            
        return ans
