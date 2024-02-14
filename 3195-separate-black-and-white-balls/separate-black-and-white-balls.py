class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        lis = list(s)
        l = 0
        r = n-1
        swaps = 0
        while l < r:
            if lis[l] == "1" and lis[r] == "0":
                lis[l],lis[r]=lis[r],lis[l]
                
                swaps += (r-l)
                l += 1
                r -= 1
            elif lis[l] == "1" and lis[r] == "1":
                r-=1
            elif lis[l] == "0" and lis[r] == "0":
                l += 1
            else:
                l += 1
                r -= 1
        return swaps

            

                