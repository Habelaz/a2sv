class Solution:
    def reverseWords(self, s: str) -> str:
        # w=list(s.split())
        # w.reverse()
        # z=" ".join(w)
        # return z
        w = list(s.split())
        l , r = 0 , len(w) - 1
        n=''
        while r >= l:
            n += w[r]
            n += " "
            r -= 1
        return n.strip()