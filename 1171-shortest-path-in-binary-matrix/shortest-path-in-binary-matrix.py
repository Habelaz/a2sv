class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        directions = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
        q = deque()
        q.append([0,0,1])
        visited = set()
        visited.add((0,0))
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        while q:
            row,col,length = q.popleft()
            if row == col == len(grid) -1:
                return length

            for rc,cc in directions:
                nr = row + rc
                nc = col + cc

                if inbound(nr,nc) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append([nr,nc,length+1])
        return -1
        

