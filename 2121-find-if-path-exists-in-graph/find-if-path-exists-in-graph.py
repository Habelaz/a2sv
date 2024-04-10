class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # def dfs(node):
        #     if node == destination:
        #         return True
            
        #     visited.add(node)
        #     for neighbour in graph[node]:
        #         if neighbour not in visited:
        #             found = dfs(neighbour)
        #             if found:
        #                 return True
        #     return False

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    
                    stack.append(neighbour)
        return False
        # return dfs(source)