class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1/x

            return (pow(x,n//2)**2) * pow(x,n%2)

        return(pow(x,n))             