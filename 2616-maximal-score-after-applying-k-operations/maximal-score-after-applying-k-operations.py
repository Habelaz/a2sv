class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        ans = 0
        for i in range(k):
            num = heapq.heappop(nums)
            ans += -num
            heapq.heappush(nums,-ceil(-num/3))
        
        return ans