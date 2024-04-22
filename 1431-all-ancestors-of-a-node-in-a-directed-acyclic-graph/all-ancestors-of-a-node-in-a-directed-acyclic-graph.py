class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        indegree = [0 for i in range(n)]

        for start,end in edges:
            graph[start].append(end)
            indegree[end] += 1

        q = deque()
        for i,inc in enumerate(indegree):
            if inc == 0:
                q.append(i)
        ans = [set() for i in range(n)]
        while q:
            node = q.popleft()

            for nbr in graph[node]:
                ans[nbr].add(node)
                ans[nbr].update(ans[node])
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    q.append(nbr)

        ans = [sorted(list(li)) for li in ans]
        return ans