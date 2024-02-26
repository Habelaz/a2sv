class Solution:
    def splitString(self, s: str) -> bool:
        stack = []
        def split(idx):
            
            if idx >= len(s):
                return len(stack) >= 2

            for i in range(idx,len(s)):
                val = int(s[idx:i+1])
                if len(stack) == 0 or val == stack[-1] - 1:
                    stack.append(val)
                    if split(i+1):
                        return True
                
                    stack.pop()
            return False
        return split(0)
                