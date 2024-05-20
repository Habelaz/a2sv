class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        pali = []
        def backtrack(i):
            if i >= len(s):
                ans.append(pali.copy())
                return

            for j in range(i,len(s)):
                curr = s[i:j+1]
                if curr == curr[::-1]:
                    pali.append(curr)
                    backtrack(j+1)
                    pali.pop()

        backtrack(0)
        return ans