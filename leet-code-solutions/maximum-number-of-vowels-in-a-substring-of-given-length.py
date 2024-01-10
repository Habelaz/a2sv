class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        l,r = 0,k
        v = 0
        for i in range(k):
            if s[i] in vowels:
                v += 1
        max_v = v
        while r < len(s):
            if s[r] in vowels:
                v += 1
            if s[l] in vowels:
                v -= 1
            max_v = max(max_v,v)
            # print(l,r,v)
            l += 1
            r += 1
        
        return max_v
