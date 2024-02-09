class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        pref = [0] * (len(nums) + 1)

        for start,end in requests:
            pref[start] += 1
            pref[end+1] -= 1

        acc = 0
        for i in range(len(pref)):
            acc += pref[i]
            pref[i] = acc
        pref.sort(reverse = True)
        nums.sort(reverse = True)

        ans = 0
        for i in range(len(nums)):
            ans += pref[i] * nums[i]
       
        # print(nums)
        return ans % mod