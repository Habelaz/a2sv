class Solution:
    def longestDecomposition(self, text: str) -> int:
        if len(set(text)) == 1:
            return len(text)
        txt1 = ''
        txt2 = ''
        n = len(text)
        # l,r = 0,len(text)-1
        count = 0
        for i in range(len(text)):
            txt1 += text[i]
            txt2 += text[n-i-1]

            if txt1 == txt2[::-1]:
                count += 1
                txt1 = ''
                txt2 = ''
        
        return count
