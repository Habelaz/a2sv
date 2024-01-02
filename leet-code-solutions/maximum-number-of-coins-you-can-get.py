class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans = 0
        cnt = 0
        i = 1
        while cnt < (len(piles)/3):
            ans += piles[i]
            i += 2
            cnt += 1
            
        return ans
        
        