class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        d = 0
        for key,val in count.items():
            if d == 0:
                d = val
            else:
                d = math.gcd(d,val)
        return True if d > 1 else False