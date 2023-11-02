class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, 1
        pairs = set()
        
        while r < n:
            diff = nums[r] - nums[l]
            
            if diff == k:
                pairs.add((nums[l], nums[r]))
                l += 1
                r += 1
            elif diff < k:
                r += 1
            else:
                l += 1
        
            # Move l and r forward if they point to the same number
            if l == r:
                r += 1
        
        return len(pairs)
        