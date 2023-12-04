class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        x = min(start, destination)
        y = max(start, destination)
        return min(sum(distance[x:y]), sum(distance[:x] + distance[y:]))