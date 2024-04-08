class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for i in range(n)] 
        
        def dfs(u):
            for v in range(n):
                if isConnected[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    dfs(v)

        count = 0
        for i in range(n):
            if not visited[i]:
                # visited[i] = True
                count += 1
                dfs(i)

        return count