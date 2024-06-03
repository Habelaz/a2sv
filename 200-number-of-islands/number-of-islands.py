class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j):
            stack = [(i, j)]
    
            while stack:
                ci, cj = stack.pop()
                
                if grid[ci][cj] == '0':
                    continue

                grid[ci][cj] = '0'
                
                for rc, cc in directions:
                    nr = ci + rc
                    nc = cj + cc
                    if inbound(nr, nc) and grid[nr][nc] == '1':
                        stack.append((nr, nc))
            return
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1

        return count