class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        arr = [(efficiency[i],speed[i]) for i in range(len(speed))]
        arr.sort(reverse = True)

        ans,curr= 0,0
        heap = []

        for e,s in arr:
            curr += s
            heappush(heap,s)

            if len(heap) > k:
                curr -= heappop(heap)

            ans = max(ans,e*curr)

        return ans % mod

