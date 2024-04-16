class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = nlargest(k,nums)
        
        return nums.pop()