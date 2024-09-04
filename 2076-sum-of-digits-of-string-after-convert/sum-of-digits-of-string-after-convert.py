class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ""
        for c in s:
            ans += str(ord(c)-ord('a')+1)

        while k > 0:
            temp = 0
            for c in ans:
                temp += int(c)
            ans = str(temp)
            k -= 1
        return int(ans)