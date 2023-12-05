class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        output =[]
        for word in words:
            # word.lower()
            ans =[]
            for char in word.lower():
                if char in row1:
                    ans.append(1)
                elif char in row2:
                    ans.append(2)
                elif char in row3:
                    ans.append(3)
            if len(set(ans)) == 1:
                output.append(word)
        return output
        
