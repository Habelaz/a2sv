class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        k = max(costs)
        counts = [0]*(k+1)
        for i in costs:
            counts[i] += 1
        so = []
        for i in range(k+1):
            so.extend([i] * counts[i])
        print(so)
        cnt = 0
        summ = 0
        i = 0
        # while summ <= coins and i < len(counts):
        #     summ += (counts[i] * i)
        #     print(summ)
        #     if counts[i] != 0 and summ <= coins:
        #         cnt += 1 *counts[i]
        #     i += 1
        while summ <= coins and i < len(so):
            summ += so[i]
            i += 1
            if summ <= coins:
                cnt += 1
        return cnt
        
            