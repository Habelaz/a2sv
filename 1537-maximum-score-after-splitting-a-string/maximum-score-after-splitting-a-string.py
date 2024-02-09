class Solution:
    def maxScore(self, s: str) -> int:
        pref = [0] * len(s)
        ans = 0
        cnt = s.count('1')
        zeros,ones = 0,0

        for i in range(len(s)-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            ans = max(ans, zeros + (cnt - ones))

        return ans
        
        