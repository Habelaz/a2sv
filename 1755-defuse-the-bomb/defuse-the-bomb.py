class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0 :
            return ans
        if k > 0:
            s = sum(code[1:k+1])
            for i in range(n):
                ans[i] = s
                s = s - code[(i+1)%n] + code[(i+1+k)%n]
        
        if k < 0:
            s = sum(code[k:])
            for i in range(n):
                ans[i] = s
                s = s + code[i%n] - code[(i+k)%n]
        
        return ans