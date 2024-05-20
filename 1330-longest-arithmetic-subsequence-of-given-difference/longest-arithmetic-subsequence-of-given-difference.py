class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        longest = 0
        for n in arr:
            dp[n] = dp[n-difference] + 1
            longest = max(longest,dp[n])

        return longest