class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        seen = set()
        ans = 0
        for c in s:
            if c not in seen:
                first,last = s.find(c),s.rfind(c)
                if last > first + 1:
                    ans += len(set(s[first+1:last]))
                # ans = max(ans,last - first - 1)
            seen.add(c)
        return ans