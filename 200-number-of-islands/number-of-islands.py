class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for _ in range(len(grid))]
        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j):
            
            if grid[i][j] =='0':
                return
            
            for rc,cc in directions:
                nr = i + rc
                nc = j + cc
                if inbound(nr,nc) and not visited[nr][nc]:
                    visited[nr][nc] = True
                    dfs(nr,nc)
            return
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    count += 1

        return count