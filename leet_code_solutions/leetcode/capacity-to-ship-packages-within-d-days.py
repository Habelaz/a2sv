class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def helper(mid):

            days = 1
            curr = 0

            for weight in weights:
                if curr + weight > mid:
                    days += 1
                    curr = weight
                else:
                    curr += weight
            return days
        low,high = max(weights),sum(weights)

        while low <= high:
            mid = low + (high - low) // 2
            if helper(mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        
        return low