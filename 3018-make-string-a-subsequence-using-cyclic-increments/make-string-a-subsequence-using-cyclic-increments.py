class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l = len(str2)
        ind = 0
        for c in str1:
            if ind < l and (ord(str2[ind]) - ord(c)) % 26 < 2:
                ind += 1
        
        return ind == l