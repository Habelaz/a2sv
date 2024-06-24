class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        count = 0
        
        for n in num:
            while count < k and stack and int(stack[-1]) > int(n) :
                stack.pop()
                count += 1
            stack.append(n)
        
        while count < k:
            stack.pop()
            count += 1
        
        ans = ''.join(stack).lstrip('0')  # Remove leading zeros
        return ans if ans else '0'