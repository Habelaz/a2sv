class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] < len(nums):
                
                pos = nums[i] - 1
                if pos != i and nums[i] != nums[pos]:
                    nums[pos],nums[i] = nums[i],nums[pos]
                else:
                    i += 1
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        return len(nums) + 1