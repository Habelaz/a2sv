class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        ans = [None]*len(s)
        for i in s:
            curr = int(i[-1])
            ans[curr - 1] = i[:-1]
            # print(ans)
        return ' '.join(ans)