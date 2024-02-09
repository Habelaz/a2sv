class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = [0] * (len(nums)+1)
        suff = [0] * (len(nums)+1)

        acc = 0
        for i in range(len(nums)):
            pref[i] = acc
            acc += nums[i]

        acc = 0
        for i in range(len(nums)-1,-1,-1):
            suff[i] = acc
            acc += nums[i]
        ans = []
        for i in range(len(nums)):
            x = (nums[i]*i - pref[i]) + suff[i] - (nums[i]*(len(nums)-i-1))
            ans.append(x)
        return ans