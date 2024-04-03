class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(node,visited):
            if node == destination:
                return True
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour,visited)
                    if found:
                        return True
            return False

        graph = defaultdict(list)

        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        return dfs(source,visited)