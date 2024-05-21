class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return True
        n = len(piles)
        summ = sum(piles)
        @cache
        def dp(i,j,total,turn):
            if j <= i:
                return total < summ 
            if not turn:
                return dp(i+1,j,total + piles[i],not turn) or dp(i,j-1,total+piles[j],not turn)
            else:
                return dp(i+1,j,total + piles[i],turn) or dp(i,j-1,total+piles[j],turn)
        return dp(0,n-1,0,False)