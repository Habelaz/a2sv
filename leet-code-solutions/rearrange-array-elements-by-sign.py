class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # pos = [num for num in nums if num > 0]
        # neg = [num for num in nums if num < 0]
        # ans = []
        # for i in range(len(pos)):
        #     ans.append(pos[i])
        #     ans.append(neg[i])
        # return ans
        l,r = 0,1
        ans = [None] * len(nums)
        for num in nums:
            if num > 0:
                ans[l] = num
                l += 2
            else:
                ans[r] = num
                r += 2
        return ans