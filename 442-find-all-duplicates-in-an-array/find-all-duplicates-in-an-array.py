class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ans = set()

        i = 0
        while i < len(nums):
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i],nums[pos] = nums[pos],nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != (i+1) :
                ans.add(nums[i])
        return ans
        
            
        