class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[:2]
        for i in range(2,len(s)):
            if s[i-2] == s[i-1] == s[i]:
                continue
            else:
                ans += s[i]
        return ans
        
