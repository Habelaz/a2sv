class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n =len(set(nums))
        ans = 0
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) == n:
                ans += (len(nums) - r)
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

        return ans

            