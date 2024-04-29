class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = [[] for i in range(n)]
        incoming = [0 for i in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            incoming[u] += 1
            incoming[v] += 1

        q = deque()
        for i in range(n):
            if incoming[i] == 1:
                q.append(i)
        
        while n > 2:
            n -= len(q)
            for i in range(len(q)):
                node = q.popleft()
                for nbr in graph[node]:
                    incoming[nbr] -= 1

                    if incoming[nbr] == 1:
                        q.append(nbr)
            

        return list(q)