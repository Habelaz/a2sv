class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed = list(allowed)
        ans = 0 
        for word in words:
            is_allowed = True
            for c in word:
                if c not in  allowed:
                    is_allowed = False
                    break
            ans += 1 if is_allowed else 0
        return ans