class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = ''
        
        for i in range(len(palindrome)//2 ):
            if ord(palindrome[i]) > ord('a'):
                ans += palindrome[:i] + 'a' + palindrome[i+1:]
                return ans
        if len(set(palindrome)) <= 2 and len(palindrome) > 1:
            x = ord(palindrome[-1])
            if x == ord('a'):
                ans += palindrome[:-1] + chr(x+1)
        
        return ans