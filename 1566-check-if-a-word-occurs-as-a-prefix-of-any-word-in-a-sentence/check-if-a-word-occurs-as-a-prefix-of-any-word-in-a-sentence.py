class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = list(sentence.split())
        n = len(searchWord)
        for i in range(len(sentence)):
            if searchWord in sentence[i] and searchWord == sentence[i][:n]:
                return i + 1
        return -1