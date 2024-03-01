class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n % 3 != 0:
        #     return False
        def pow(n):
            if n == 1:
                return True
            elif n%3 == 0 and n!=0:
                return pow(n//3)
            # return False
        return pow(n)
            