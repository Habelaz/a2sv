class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = {0:1}
        curr_sum = 0
        ans = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            diff = curr_sum - goal

            ans += pref.get(diff,0)
            pref[curr_sum] = pref.get(curr_sum,0)+1
            # print(diff,pref)
        return ans