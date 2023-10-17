class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for i in t:
            if count < len(s) and s[count] == i:
                count += 1

        return count == len(s)
