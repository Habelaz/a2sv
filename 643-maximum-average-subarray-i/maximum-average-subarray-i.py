class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            raise ValueError("Subarray length k cannot be greater than array length")

        max_average = sum(nums[:k]) / k
        current_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            current_average = current_sum / k
            max_average = max(max_average, current_average)

        return max_average