class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = [[num,i] for i,num in enumerate(nums)]
        heapify(arr)
        for i in range(k):
            curr = heapq.heappop(arr)
            curr[0] *= multiplier
            heapq.heappush(arr,curr)
        
        while arr:
            n,i = arr.pop()
            nums[i] = n
        return nums