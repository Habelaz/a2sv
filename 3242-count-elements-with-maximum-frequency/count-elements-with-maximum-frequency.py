class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxx = max(count.values())
        ans = 0
        for x in count.values():
            if x == maxx:
                ans += maxx

        return ans