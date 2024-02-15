class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key = lambda x: x[1])
        # print(points)
        arrow = 0
        end = -1*float('inf')
        for i in range(len(points)):
            if points[i][0] > end:
                arrow += 1
                end = points[i][1]

        return arrow
        