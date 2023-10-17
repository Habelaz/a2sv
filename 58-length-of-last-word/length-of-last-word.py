class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newl=s.split()
        x=newl[-1]
        return len(x)