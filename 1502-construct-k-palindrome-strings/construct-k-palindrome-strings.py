class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        count = Counter(s)
        odds = 0
        for key,val in count.items():
            if val % 2 != 0:
                odds += 1

        if odds > k:
            return False
        else:
            return True

        