class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0 
        ans = ''
        reverse = False
        while l < len(s) :
            x = s[l:l+k]
            if reverse:
                ans += x
                reverse = False

            else:
                x = x[::-1]
                ans += x
                print(x)
                reverse = True
            l += k
            
        ans += s[l:]
        return ans
            


            
