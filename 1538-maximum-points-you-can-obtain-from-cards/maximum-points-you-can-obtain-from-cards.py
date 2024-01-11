class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        summ = sum(cardPoints[:k])
        max_s = summ
        n = len(cardPoints)
        for r in range(k):
            summ += cardPoints[n-1-r]
            summ -= cardPoints[k-1-r]
            if summ > max_s:
                max_s = summ
        return max_s