class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def helper(p,t):
            return ((p+1)/(t+1)) - (p/t)

        heap = []
        for p,t in classes:
            ratio_diff = helper(p,t)
            heap.append((-ratio_diff,p,t))

        heapq.heapify(heap)
        if heap[0][0] == 0:
            return 1
        for i in range(extraStudents):
            ratio_diff,p,t = heapq.heappop(heap)
            heapq.heappush(heap,(-helper(p+1,t+1),p+1,t+1))

        ans = 0
        for pr,p,t in heap:
            ans += (p/t)

        return ans/len(classes)


