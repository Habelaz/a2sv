class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        summ = sum(nums[:k])
        ans = summ
        for i in range(k,n):
            summ += nums[i]
            summ -= nums[i - k]  

            if summ > ans:
                ans = summ
        return (ans)/k