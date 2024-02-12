class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # nums.append(0)
        mapp = {0:1}
        res,ans = 0,0

        for i in nums:
            res += i
            div = res%k

            if div in mapp:
                ans += mapp[div]
                mapp[div] += 1
            else:
                mapp[div] = 1
        return ans