class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        incoming = [0 for i in range(n)]

        for u,v in edges:
            graph[u].append(v)
            incoming[v] += 1

        ans = [i for i,inc in enumerate(incoming) if inc == 0]
        
        return ans[0] if len(ans) == 1 else -1