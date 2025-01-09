class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        ans = 0 
        for w in words:
            if pref in w and pref == w[:n]:
                ans += 1
        return ans