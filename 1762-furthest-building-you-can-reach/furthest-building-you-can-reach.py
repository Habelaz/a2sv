class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1,len(heights)):
            diff = heights[i]-heights[i-1]

            if diff <= 0:
                continue
            heappush(heap,-diff)
            bricks -= diff

            if bricks < 0:
                if ladders == 0:
                    return i - 1
                ladders -= 1
                bricks += -heappop(heap)
        return len(heights) - 1

        