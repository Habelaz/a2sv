class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=bin(x^y)
        return x.count("1")