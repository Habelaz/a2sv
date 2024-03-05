class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = True
        s = list(s.lower())
        new = []
        for i in range(len(s)):
            if s[i].isalnum():
                new.append(s[i])
        l = 0
        r = len(new) - 1
        while l <= r:
            if new[l] != new[r]:
                flag = False
                break
            l += 1
            r -= 1
        return flag