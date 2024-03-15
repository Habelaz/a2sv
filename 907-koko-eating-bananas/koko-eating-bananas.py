class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def helper(mid):
            hour = 0
            curr = 0
            for b in piles:
                if b < mid:
                    hour += 1
                else:
                    hour += ceil(b/mid)
            return hour

        low = 1
        high = max(piles)

        while low <= high :
            mid = low + (high - low) // 2
            # print(helper(mid),mid)
            if helper(mid) <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low
