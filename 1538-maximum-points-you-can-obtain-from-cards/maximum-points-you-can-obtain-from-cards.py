class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = len(cardPoints) - k
        summ = sum(cardPoints[r:])
        max_s = summ
        
        n = len(cardPoints)
        while r < n:
            summ += (cardPoints[l] - cardPoints[r])
            l += 1
            r += 1
            if summ > max_s:
                max_s = summ
        return max_s
        # for r in range(k):
        #     summ += cardPoints[n-1-r]
        #     summ -= cardPoints[k-1-r]
        #     if summ > max_s:
        #         max_s = summ
        return max_s