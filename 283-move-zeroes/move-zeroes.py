class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=i+1
        n=len(nums)
        while j < n:
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
            if nums[i] != 0:
                i +=1
            j += 1