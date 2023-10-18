class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_count = {}
        
        for num in nums:
            if num in num_count:
                duplicated = num
            else:
                num_count[num] = 1

        for i in range(1, n + 1):
            if i not in num_count:
                missing = i

        return [duplicated, missing]