class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        vals = count.values()
        d = math.gcd(*vals)
        return True if d > 1 else False