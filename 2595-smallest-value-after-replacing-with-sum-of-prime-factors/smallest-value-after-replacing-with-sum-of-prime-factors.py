class Solution:
    
    
    def smallestValue(self, n: int) -> int:
        def prime_factors(n):
            i = 2
            factors = []
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.append(i)
            if n > 1:
                factors.append(n)
            return factors

        num = n
        seen = set()
        while num > 0:
            factors = prime_factors(num)
            if len(factors) == 1:
                return factors[0]
            num = sum(factors)
            if num in seen:
                break
            seen.add(num)
        return num
            
        
        