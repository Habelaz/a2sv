class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        longest = 0
        for i in words:
            longest = max(longest,len(i))
        
        vertical = ['' for _ in range(longest)]
        for row in range(longest):
            for word in words:
                if row < len(word):
                    vertical[row] += word[row]
                else:
                    vertical[row] += " "
            vertical[row] = vertical[row].rstrip()
            
        return vertical