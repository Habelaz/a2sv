class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        summ = 0
        if numOnes >= k:
            return k
        else:
            summ += numOnes
            k -= numOnes
            if k > numZeros:
                k -= numZeros
                while k:
                    summ -= 1
                    k -= 1
        return summ
