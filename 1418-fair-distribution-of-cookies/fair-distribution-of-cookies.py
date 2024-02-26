class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0]*k
        i = 0
        minn = float('inf')
        def distribute(i):
            nonlocal minn
            if i == len(cookies):
                minn = min(minn,max(bucket))
                return 
            if minn < max(bucket):
                return
            
            for j in range(k):
                bucket[j] += cookies[i]
                distribute(i+1)
                bucket[j] -= cookies[i]

        distribute(0)
        return minn