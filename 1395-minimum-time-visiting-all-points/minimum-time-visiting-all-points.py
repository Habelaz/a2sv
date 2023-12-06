class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def time_to_travel(point1, point2):
            dx = abs(point1[0] - point2[0])
            dy = abs(point1[1] - point2[1])
            return max(dx, dy)

        total_time = 0
        for i in range(len(points) - 1):
            total_time += time_to_travel(points[i], points[i + 1])

        return total_time