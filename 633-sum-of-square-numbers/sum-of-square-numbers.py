class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=math.ceil(c**0.5)
        while l <= r:
            if l*l + r*r == c:
                return True
                l += 1
                r -= 1
            if l*l + r*r > c:
                r-= 1
            else:
                l += 1
        return False
        