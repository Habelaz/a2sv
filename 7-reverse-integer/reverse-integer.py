class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            sign=1
        else:
            sign=-1
        x=abs(x)
        re_str=str(x)[::-1]
        re_int=sign * int(re_str)
        
        if re_int > (2**31 -1) or re_int < -(2**31):
            return 0
        return re_int