class Solution:
    def reverseWords(self, s: str) -> str:
        w=list(s.split())
        w.reverse()
        z=" ".join(w)
        return z