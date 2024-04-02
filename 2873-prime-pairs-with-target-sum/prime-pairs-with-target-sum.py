class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        if n <= 2:
            return []
            
        primes = [True for i in range(n+1)]
        primes[0] = primes[1] = False
        d = 2
        while d*d <= n:
            if primes[d]:
                j = d*d
                while j <= n:
                    primes[j] = False
                    j += d
            d += 1
        ind = [i for i in range(len(primes)) if primes[i]]

        l,r = 0, len(ind) - 1
        ans = []
        while l <= r:
            if ind[l] + ind[r] == n:
                ans.append([ind[l],ind[r]])
                r -= 1
                l += 1
            elif ind[l] + ind[r] < n:
                l += 1
            else:
                r -= 1
        return ans



