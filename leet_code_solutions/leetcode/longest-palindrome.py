class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = Counter(s)
        odd = False
        ans = 0
        for c in s:
            
            if s[c] % 2 == 0:
                ans += s[c]
            else:
                ans += (s[c]-1)
                odd = True

        if odd:
            ans += 1
        return ans
