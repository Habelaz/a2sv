class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            nums[i] = acc
        pref = [0] + nums
        for i in range(1,len(pref)):
            if pref[i-1] == pref[-1] - pref[i]:
                return i - 1
        else:
            return -1

