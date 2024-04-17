class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            if x == y:
                continue
            else:
                heappush(stones,y - x)
        return -stones[0] if stones else 0