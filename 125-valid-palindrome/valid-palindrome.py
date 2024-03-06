class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = [c.lower() for c in s if c.isalnum()]
        new = list(reversed(alpha))
        return new == alpha