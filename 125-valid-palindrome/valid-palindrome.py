class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [char.lower() for char in s if char.isalnum()]
        clean = ''.join(clean)
        if clean == clean[::-1]:
            return True
        else:
            return False