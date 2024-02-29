class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        pref = [0] * len(nums)
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            pref[i] = acc

        res = nums[0]
        for i in range(len(pref)):
            if math.ceil(pref[i] / (i+1)) > res:
                res = ceil(pref[i]/(i+1))
        return res
