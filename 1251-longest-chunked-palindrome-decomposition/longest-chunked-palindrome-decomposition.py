class Solution:
    def longestDecomposition(self, text: str) -> int:
        if len(set(text)) == 1:
            return len(text)
        txt1 = ''
        txt2 = ''
        l,r = 0,len(text)-1
        count = 0
        
        while l < r:
            txt1 += text[l]
            txt2 += text[r]
            if text[r] == txt1[0]:
                if txt1 == txt2[::-1]:
                    txt1 = ''
                    txt2 = ''
                    count += 2
            
            l += 1
            r -= 1
        if l == r and len(txt1) == 0:
            count += 1
        if len(txt1) != 0:
            count += 1
        
        return count
