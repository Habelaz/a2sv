class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1] * (len(nums) + 1)
        i = 0
        while i < len(nums):
            
            pos = nums[i] 
            if pos != i:
                arr[pos] = nums[i]
            else:
                arr[i] = pos
            
            i += 1
        print(arr)
        for ind,num in enumerate(arr):
            if num == -1:
                return ind
            
        


        