class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        n,m = len(mat),len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf')
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m
        ans = [0 * m] * n 
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for rc,cc in directions:
                    nr = r + rc
                    nc = c + cc

                    if inbound(nr,nc) and mat[nr][nc] > mat[r][c] +1 :
                        q.append((nr,nc))
                        mat[nr][nc] = mat[r][c] + 1
        return mat

