class Solution:
    def maxScore(self, s: str) -> int:
        count = s.count('1')
        ans = 0 
        zeros,ones =0,0
        for i in range(len(s)-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            ans = max(ans,zeros + (count - ones))
        
        return ans