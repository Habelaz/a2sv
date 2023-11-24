class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        l = 0
        for r in  range(len(nums)):
            if nums[l] != nums[r]:
                l += 1
            # else:
                nums[l] = nums[r]
        return l + 1