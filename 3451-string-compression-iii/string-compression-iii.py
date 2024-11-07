class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1

        for i in range(len(word) - 1):
            if word[i] == word[i + 1] and count < 9:
                count += 1
            else:
                comp += str(count) + word[i]
                count = 1

        comp += str(count) + word[-1]
        return comp