class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for i in range(len(s)):
            if s[i] =="(" or locked[i] == '0':
                stack.append("(")
            else :
                if not stack:
                    return False
                else:
                    stack.pop()

        stack = []
        for i in range(len(s)-1, -1 ,-1):
            if s[i] ==")" or locked[i] == '0':
                stack.append(")")
            else :
                if not stack:
                    return False
                else:
                    stack.pop()
        return True