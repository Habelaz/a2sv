class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = sum(1 for candidate in candidates if candidate & (1 << i))
            ans = max(ans, count)
        return ans