class Solution:
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def dfs(r,c):
            if (r,c) == destination:
                return True
            
            for rc,cc in directions[grid[r][c]]:
                # print(visited)
                nr = r + rc
                nc = c + cc
                if inbound(nr,nc) and (nr,nc) not in visited and [-rc,-cc] in directions[grid[nr][nc]]:
                    visited.add((nr,nc))
                    found = dfs(nr,nc)
                    # print(found)
                    if found:
                        return True
            return 

        directions = {
            1:[[0,1],[0,-1]],
            2:[[-1,0],[1,0]],
            3:[[0,-1],[1,0]],
            4:[[0,1],[1,0]],
            5:[[-1,0],[0,-1]],
            6:[[-1,0],[0,1]]
        }
        
        def inbound(r,c):
            return (0 <= r < len(grid) and 0<= c < len(grid[0]))
        destination = (len(grid)-1,len(grid[0])-1)
        visited = set([(0,0)])
        return dfs(0,0)
