class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0
        for i in range(len(nums)-1):
            x = heappop(nums)
            y = heappop(nums) if len(nums) > 0 else k
            if x >= k:
                return ans
            ans += 1
            heappush(nums,min(x,y) * 2 + max(x,y))

        return ans
