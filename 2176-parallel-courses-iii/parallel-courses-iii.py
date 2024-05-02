class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for i in range(n+1)]
        incoming = [0 for i in range(n+1)]

        for prev,nextt in  relations:
            graph[prev].append(nextt)
            incoming[nextt] += 1
        
        q = []
        for i,inc in enumerate(incoming):
            if inc == 0 and i != 0:
                heappush(q,(time[i-1],i))

        ans = 0
        while q:
            
            for i in range(len(q)):
                cur_time,node = heappop(q)
                ans = max(ans,cur_time)
                for nbr in graph[node]:
                    incoming[nbr] -= 1

                    if incoming[nbr] == 0:
                        heappush(q,(cur_time + time[nbr-1],nbr))

        return ans
        