class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,curr_sum =0,0
        pref={0:1}

        for i in range(len(nums)):
            curr_sum += nums[i]
            diff =curr_sum - k

            res += pref.get(diff,0)
            pref[curr_sum] = 1 + pref.get(curr_sum,0)

        return res