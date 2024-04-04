class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited =[[false for i in range(len(grid))] for j in range(len(grid[0]))]
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r,c):
            if grid[r][c] == '0':
                return
            for rc,cc in directions:
                nr = r + rc
                nc = c + cc
                
                if inbound(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    dfs(nr,nc)
            return
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == '1' and (i,j) not in visited:
                    # print(1)
                    dfs(i,j)
                    count += 1
        return count