class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,curr_sum =0,0
        prefixsums={0:1}

        for i in range(len(nums)):
            curr_sum += nums[i]
            diff =curr_sum - k

            res += prefixsums.get(diff,0)
            prefixsums[curr_sum] = 1 + prefixsums.get(curr_sum,0)

        return res