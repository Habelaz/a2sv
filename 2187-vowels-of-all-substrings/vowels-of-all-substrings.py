class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0 
        n = len(word)
        vowels = ["a","e","i","o","u"]
        for i,c in enumerate(word):
            if c in vowels:
                ans += (i+1) * (n-i)
                
        return ans