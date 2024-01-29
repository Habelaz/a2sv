class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt_o = 0
        res = 0
        count = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] % 2:
                cnt_o += 1
                count = 0
            
            while cnt_o == k:
                if nums[l] % 2:
                    cnt_o -= 1
                count += 1
                l += 1
            
            res += count
        return res