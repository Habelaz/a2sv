class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        
        mask = x & -x
        group1,group2 = 0,0
        for num in nums:
            if num & mask:
                group1 ^= num
            else:
                group2 ^= num

        return [group1,group2]