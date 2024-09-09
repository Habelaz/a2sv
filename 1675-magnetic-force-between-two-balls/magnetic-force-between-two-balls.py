class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:
        positions.sort()
        low = 1
        high = floor((positions[-1] - positions[0]) / (m - 1))

        def helper(dist):
            ball_count = 1
            prev_position = positions[0]
            for position in positions:
                if position - prev_position >= dist:
                    ball_count += 1
                    if ball_count == m:
                        return True
                    
                    prev_position = position
            
            return False


        while low < high:
            mid = ceil((low + high) / 2)
            if helper(mid):
                low = mid 
            else:
                high = mid - 1
        
        return low