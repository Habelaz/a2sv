class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if len(nums) > 1 and nums[0] == 0:
            return False
        nums.reverse()
        l = 0
        r = 1
        flag = False
        while r < len(nums):
            if nums[r] >= (r-l):
                flag = True
                l = r
                r += 1
            else:
                r += 1
                flag = False
        return flag
