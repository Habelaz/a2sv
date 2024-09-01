class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words) -1
        while n > 0:
            if Counter(words[n])== Counter(words[n-1]):
                words.pop(n)
            n -= 1
        return words