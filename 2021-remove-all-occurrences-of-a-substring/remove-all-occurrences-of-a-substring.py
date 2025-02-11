class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part) 
        last = part[-1]
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == last and len(stack) >= n :
                st = "".join(stack[-n:]) 
                if st == part:
                    for i in range(n):
                        stack.pop()
                
        return "".join(stack)


      