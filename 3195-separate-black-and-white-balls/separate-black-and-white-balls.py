class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        ans = 0

        for num in s:
            if num == "1":
                ones += 1
            else:
                ans += ones

        return ans        