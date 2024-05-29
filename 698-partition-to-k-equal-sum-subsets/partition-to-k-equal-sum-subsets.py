class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target_sum = sum(nums) // k
        def backtrack(sums,i):
            nonlocal target_sum
            if i == len(nums):
                return True

            for j in range(k):
                if j > 0 and sums[j] == sums[j - 1]:
                    continue
                sums[j] += nums[i]
                if sums[j] <= target_sum and backtrack(sums, i + 1):
                    return True
                sums[j] -= nums[i]
            return False

        nums.sort(reverse = True)
        sums = [0] * k

        return backtrack(sums,0)

        