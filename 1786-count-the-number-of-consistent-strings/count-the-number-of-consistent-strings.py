class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        arr = [0] * 26
        for c in allowed:
            arr[ord(c) - ord('a')] = 1
        
        count = 0
        for word in words:
            is_allowed = 1
            for char in word:
                if arr[ord(char) - ord('a')] == 0:
                    is_allowed = 0
                    break
            count += is_allowed
        return count