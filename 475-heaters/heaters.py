class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        heaters.sort()
        for house in houses:
            low,high = 0,len(heaters) - 1
            min_d = float('inf')

            while low <= high:
                mid = low + (high - low) // 2
                if heaters[mid] == house:
                    min_d = 0
                    break
                elif heaters[mid] < house:
                    min_d = min(min_d,abs(heaters[mid] - house))
                    low = mid + 1
                else:
                    min_d = min(min_d,abs(heaters[mid] - house))
                    high = mid - 1
            # print(low)
            # min_d = min(min_d,abs(heaters[low]) - house)
            radius = max(radius,min_d)
        return radius
                    