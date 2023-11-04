class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0
        n=len(height)
        l,r = 0 , n - 1
        while l < r :
            water = min(height[l],height[r])*(r-l)
            if water > most_water:
                most_water = water
            elif height[l] < height[r]:
                l += 1
            else:
                r-= 1
        return most_water