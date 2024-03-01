class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
            
        pref = [0] *( len(weights) - 1)
        for i in range(1,len(weights)):
            pref[i-1] = weights[i] + weights[i-1]
        pref.sort()
        minn = sum(pref[:k-1])
        maxx = sum(pref[-k+1:])
        # minn = 0
        # maxx = 0
        # for i in range(k-1):
        #     minn += pref[i]
        #     maxx += pref[len(pref)-i-1]
        
        return maxx - minn