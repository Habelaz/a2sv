class Solution:
    def myPow(self, x: float, n: int) -> float:
        # sys.setrecursionlimit((2**31)-1)
        # if n >= 0:
        #     def pow(x,n,cnt):
        #         if n >= 0:
        #             if cnt >= n:
        #                 return 1
        #             return x * pow(x,n,cnt+1)
        #     cnt = 0
        #     return pow(x,n,cnt)
        # else:
        #     x = 1/x
        #     def nepow(x,n,cnt):
        #         if cnt <= n:
        #             return 1
                
        #         return x * nepow(x,n,cnt-1)
        
        #     cnt = 0
        #     return nepow(x,n,cnt)
        return x**(n)
        
            