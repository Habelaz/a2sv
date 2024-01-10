class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        ans = set()
        l = 0
        
        for r in range(n):
            if s[r] not in ans:
                ans.add(s[r])
                maxLength = max(maxLength,r - l + 1)
            else:
                while s[r] in ans:
                    ans.remove(s[l])
                    l += 1
                ans.add(s[r])
        return maxLength


