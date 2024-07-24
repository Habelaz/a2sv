class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def inbound(r,c):
            return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        
        store = {}
        def dfs(r,c,path):
            if (r,c) in store:
                return store[(r,c)]

            length = 0
            for x,y in directions:
                nr = r + x
                nc = c + y
                if inbound(nr,nc) and matrix[r][c] < matrix[nr][nc]:
                    length = max(length,dfs(nr,nc,path + 1))
            store[(r,c)] = length + 1
            return length + 1
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,dfs(i,j,1))
        
        return ans