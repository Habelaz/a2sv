class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        print(graph)
        distances = {i: float('inf') for i in range(1,n+1)}
        distances[k] = 0
        heap = [(0, k)]

        while heap:
            dist,node = heapq.heappop(heap)
            for child,weight in graph[node]:
                distance = dist + weight
                if distance < distances[child]:
                    distances[child] = distance
                    heapq.heappush(heap,(distance,child))
        ans = max(distances.values())         
        return ans if ans != float('inf') else -1