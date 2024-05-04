class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        x = 0
        for n in nums:
            x ^= n
        x ^= k
        ans = 0
        while x>0:
            if x & 1 == 1:
                ans += 1
            x >>= 1
        return ans