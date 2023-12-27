class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxx = 0
        count = 0

        for i in range(len(flips)):
            # maxx = max(maxx,flips[i])
            if maxx < flips[i]:
                maxx = flips[i]
            if maxx == i+1:
                count += 1
        return count