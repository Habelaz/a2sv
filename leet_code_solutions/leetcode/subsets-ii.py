class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        def subsets(i):

            if i <= len(nums):
                if subset not in ans:
                    ans.append(subset[:])
            
            for i in range(i,len(nums)):
                
                subset.append(nums[i])
                subsets(i+1)
                subset.pop()
        subsets(0)
        return ans