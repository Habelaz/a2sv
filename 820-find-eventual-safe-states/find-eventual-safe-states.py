class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        q = deque()
        # graph_n = defaultdict(list)
        
        # for i in range(len(graph)):
        #     for j in graph[i]:
        #         graph_n[j].append(i)

        colors = [0 for i in range(len(graph))]
        ans = []
        def dfs(node):
            if colors[node] == 1:
                return False
            colors[node] = 1

            for nbr in graph[node]:
                if colors[nbr] == 2:
                    continue
                if not dfs(nbr):
                    return False

            colors[node] = 2
            ans.append(node)
            return True

        for i in range(len(graph)):
            if colors[i] != 2:
                dfs(i)
        return sorted(ans)

        


            
