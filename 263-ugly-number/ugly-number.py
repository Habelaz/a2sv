class Solution:
    def isUgly(self, n: int) -> bool:
        primes = []
        if n <= 0:
            return False
        d = 2
        while d*d <= n:
            while n % d == 0:
                primes.append(d)
                n //= d
            d += 1
        if n > 1:
            primes.append(n)
        # print(primes)
        st = {2,3,5}

        primes =set(primes)
        for p in primes:
            if p not in st:
                return False
        return True