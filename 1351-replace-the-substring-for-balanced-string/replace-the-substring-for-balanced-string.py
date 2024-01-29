class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = Counter(s)
        result = n  
        l = 0
        
        for r in range(n):
            count[s[r]] -= 1
    
            while l < n and all(n // 4 >= count[char] for char in 'QWER'):
                result = min(result, r - l + 1)
                count[s[l]] += 1
                l += 1
        
        return result