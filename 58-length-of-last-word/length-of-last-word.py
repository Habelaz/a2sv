class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newl=s.split()
        
        return len(newl[-1])