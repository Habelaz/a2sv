class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def checker(n):
            days, curr = 1,0
            for w in weights:
                if curr + w > n:
                    days += 1
                    curr = w
                else:
                    curr += w
            return days

        low,high = max(weights),sum(weights)
        while low <= high:
            mid = low + (high - low) // 2
            if checker(mid) > days:
                low = mid + 1
            else:
                high = mid - 1
        return low