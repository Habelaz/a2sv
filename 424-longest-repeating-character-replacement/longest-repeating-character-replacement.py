class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        count = {}
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if count[s[r]] > max_count:
                max_count = count[s[r]]

            if (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1

            if r-l+1 > max_length:
                max_length = r-l+1

        return max_length