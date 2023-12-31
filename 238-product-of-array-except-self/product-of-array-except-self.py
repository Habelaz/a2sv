class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer = [1] * n
        prefix_product = 1
        for i in range(n):
            answer[i] *= prefix_product
            prefix_product *= nums[i]
        sufix_product = 1
        for i in range(n-1,-1,-1):
            answer[i] *= sufix_product
            sufix_product *= nums[i]
        return answer