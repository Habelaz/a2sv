class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target - 1 in nums:
            return nums.index(target - 1) + 1
        elif target + 1 in nums:
            x = nums.index(target + 1) - 1
            if x < 0:
                return 0
            elif x == 0:
                return 1
            return x
        # elif target + 1 in nums and nums.index(target+1) == 1:
        #     return 1
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)