class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            pos = nums[i] - 1
            if pos != i and nums[pos] != nums[i]:
                nums[pos],nums[i] = nums[i],nums[pos]
            else:
                i += 1
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
