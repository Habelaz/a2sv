class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        if len(set(nums)) == len(nums):
            return 0
        # i,j = 0,len(nums)-1
        # while i<j:
        #     if nums[i] == nums[j] and (i*j)%k == 0:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    count += 1
        return count
