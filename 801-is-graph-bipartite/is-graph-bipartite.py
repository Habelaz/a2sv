class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        def dfs(node):
            temp = True
            for neighbour in graph[node]:
                
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node] 
                    temp = temp and dfs(neighbour)
                else:
                    if color[node] == color[neighbour]:
                        return False
            return temp

        ans = True
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 0
                ans = ans and dfs(i)
        return ans

        

