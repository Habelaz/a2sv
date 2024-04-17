class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        
        if not self.maxheap or num <= -self.maxheap[0]:
            heappush(self.maxheap, -num)
            
        else:
            heappush(self.minheap, num)
           
        if len(self.maxheap) - len(self.minheap) > 1:
            heappush(self.minheap, -heapq.heappop(self.maxheap))
            
        elif len(self.minheap) - len(self.maxheap) > 1:
            heappush(self.maxheap, -heapq.heappop(self.minheap))

        

    def findMedian(self) -> float:
        
        mx = len(self.maxheap)
        mi = len(self.minheap)
        if mx > mi:
            return -self.maxheap[0]
        elif mi > mx:
            return self.minheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()