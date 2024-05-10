class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def tri(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            return tri(n-1) + tri(n-2) + tri(n-3)

        return tri(n)