class Solution:
    def removeStars(self, s: str) -> str:
        s.split()
        a = []
        for i in s:
            
            if i.isalnum():
                a.append(i)
            elif len(a) > 0:
                a.pop()

        return ''.join(a)