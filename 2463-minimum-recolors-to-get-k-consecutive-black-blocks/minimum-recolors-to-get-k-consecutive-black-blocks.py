class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            if blocks[i] == 'B':
                count += 1

        l = 0
        min_r = k - count
        for r in range(k,len(blocks)):
            if blocks[r] == 'B':
                count += 1
            if blocks[l] == 'B':
                count -= 1
            l += 1
            min_r = min(min_r,k - count)
            
        
        return min_r

        
