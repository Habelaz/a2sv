class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=''.join(filter(str.isalnum,s)).lower()
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False