class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        q = deque()
        graph_n = defaultdict(list)
        incoming = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                graph_n[j].append(i)
                incoming[i] += 1

        for i,inc in enumerate(incoming):
            if inc == 0:
                q.append(i)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)

            for nbr in graph_n[node]:
                incoming[nbr] -= 1

                if incoming[nbr] == 0:
                    q.append(nbr)
        
        return sorted(ans)

            
