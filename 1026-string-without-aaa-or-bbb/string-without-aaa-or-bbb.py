class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ""
        a_count,b_count = 0,0
        for i in range(a+b):
            if (a>b and a_count < 2) or b_count == 2:
                ans += 'a'
                a_count += 1
                b_count = 0
                a -= 1
            else:
                ans += 'b'
                b_count += 1
                a_count = 0
                b -= 1
        return ans
