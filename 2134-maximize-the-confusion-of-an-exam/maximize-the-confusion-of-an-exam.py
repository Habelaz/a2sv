class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        count = 0
        l = 0 
        for r in range(len(answerKey)):
            if answerKey[r] ==  'F':
                count += 1
            while count > k:
                if answerKey[l] == 'F':
                    count -= 1
                l += 1
            ans = max(ans,r-l+1)
        count = 0
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                count += 1
            while count > k:
                if answerKey[l] == 'T':
                    count -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
                