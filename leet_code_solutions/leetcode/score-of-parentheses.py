class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for b in s:
            if b == '(':
                stack.append(0)
            else:
                ans = max(stack.pop()*2,1)
                stack[-1] += ans

        return stack.pop()
        