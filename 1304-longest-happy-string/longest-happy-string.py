class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap,[-a,"a"])
        if b > 0:
            heapq.heappush(heap,[-b,"b"])
        if c > 0:
            heapq.heappush(heap,[-c,"c"])

        ans = ""

        while heap:

            n,s = heapq.heappop(heap)
            if len(ans) > 1 and ans[-1] == ans[-2] == s:
                if not heap:
                    break
                num,char = heapq.heappop(heap)
                ans += char
                num += 1
                if num :
                    heapq.heappush(heap,[num,char])
            else:
                ans += s
                n += 1
            if n :
                heapq.heappush(heap,[n,s])

        return ans
            