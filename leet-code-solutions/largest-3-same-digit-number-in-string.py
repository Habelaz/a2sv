class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        maxx = 0
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                ans = num[i:i+3]
                maxx = max(int(ans),maxx)
                
        if maxx == 0 and ans!='000':
            return ''
        elif ans == '000' and maxx == 0:
            return ans
        else:
            return str(maxx)

        
