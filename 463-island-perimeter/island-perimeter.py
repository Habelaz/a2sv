class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # def inbound(row,col):
        #     return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
   
        # visited = set()

        # def dfs(r,c):
        #     if not inbound(r,c) or grid[r][c] == 0:
        #         return 1
        #     if (r,c) in visited:
        #         return 0

        #     visited.add((r,c))
        #     directions = [[1,0], [0,1], [-1, 0], [0,-1]]

        #     count = 0
        #     # for ci, cj in directions:
        #     #     new_r = r + ci
        #     #     new_c = c + cj
        #     #     count += dfs(new_r, new_c)
        #     # return count
        #     return dfs(r,c+1) + dfs(r,c-1) + dfs(r-1,c) + dfs(r+1,c)


        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             return dfs(i,j)

        perim = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perim += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perim -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perim -= 2
        return perim


                
            