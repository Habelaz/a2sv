class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        nums += [0]
        mapp = defaultdict(int)
        pref = [0] * (len(nums))
        ans = 0
        acc = 0
        for i in range(len(nums)):
            pref[i] = acc
            acc += nums[i]

            if (pref[i]- goal) in mapp:
                ans += mapp[pref[i]-goal]
            mapp[pref[i]] += 1
        
        return ans
