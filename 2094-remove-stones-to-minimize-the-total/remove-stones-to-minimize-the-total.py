class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-1*p for p in piles]
        heapify(piles)
        for i in range(k):
            n = -heappop(piles)
            rem = n - n //2
            heappush(piles,-rem)
        print(piles)
        return -sum(piles)