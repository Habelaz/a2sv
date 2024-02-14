class Solution:
    def minimumSteps(self, s: str) -> int:
        blacks = 0
        ans = 0

        for i in s:
            if i == '1':
                blacks += 1
            else:
                ans += blacks

        return ans

            

                