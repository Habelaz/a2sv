class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True for i in range(n)]
        primes[0] = primes[1] = False

        i = 2
        while i * i < n:
            if primes[i]:
                j = i*i
                while j < n:
                    primes[j] = False
                    j += i
            i += 1

        count = Counter(primes)
        # print(primes,count)
        return count[True]