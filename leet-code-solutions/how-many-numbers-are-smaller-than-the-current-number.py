class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        res= []
        d = {}
        
        for ind,val in enumerate(temp):
            if val not in d:
                d[val] = ind
        for ind,val in enumerate(nums):
            res.append(d[val])
        
        return res
