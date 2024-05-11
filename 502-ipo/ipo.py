class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ipo = [(capital[i],profits[i]) for i in range(len(profits))]
        ipo.sort()
        heap = []

        i = 0
        while k > 0:
            while i < len(ipo) and ipo[i][0] <= w:
                heappush(heap,-ipo[i][1])
                i += 1

            if not heap:
                return w
            w += -heappop(heap)
            k -= 1

        return w
                
