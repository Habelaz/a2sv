class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        ans=[]
        for i in range(n):
            if nums[i] == target:
                ans.append(i)
        return ans