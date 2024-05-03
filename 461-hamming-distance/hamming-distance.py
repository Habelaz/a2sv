class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = (x ^ y)
        return x.bit_count()