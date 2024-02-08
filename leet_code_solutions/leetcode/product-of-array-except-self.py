class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer = [1] * n

        pre_product = 1
        for i in range(n):
            answer[i] *= pre_product
            pre_product *= nums[i]

        suf_product = 1
        for i in range(n-1,-1,-1):
            answer[i] *= suf_product
            suf_product *= nums[i]

        return answer
        