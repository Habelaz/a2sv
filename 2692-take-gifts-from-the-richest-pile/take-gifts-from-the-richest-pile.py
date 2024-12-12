class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-n for n in gifts]
        heapify(gifts)
        for i in range(k):
            num = int(math.sqrt(-heappop(gifts)))
            heappush(gifts,-num)
        return -sum(gifts)
