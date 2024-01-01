class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        new = [x for x,y in points]
        new.sort()
        maxx = 0

        for i in range(1,len(points)):
            area = new[i] - new[i-1]
            if maxx < area:
                maxx = area
                
        return maxx