class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        x = nums[0]
        for i in range(1,len(nums)):
            x ^= nums[i]
        x ^= k
        # ans = 0
        # while x>0:
        #     if x & 1 == 1:
        #         ans += 1
        #     x >>= 1
        # return ans
        return x.bit_count()