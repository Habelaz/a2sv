class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time,fresh = 0,0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for rc,cc in directions:
                    row = rc + r
                    col = cc + c

                    if not inbound(row,col) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

