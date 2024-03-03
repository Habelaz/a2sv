class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        sett = set(s)
        for i,c in enumerate(s):
            if c.swapcase() not in sett:
                lns1 = self.longestNiceSubstring(s[:i])
                lns2 = self.longestNiceSubstring(s[i+1:])

                return max(lns1, lns2, key=len)

        return s