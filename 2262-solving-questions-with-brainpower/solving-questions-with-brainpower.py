class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n-1,-1,-1):
            dp[i] = questions[i][0]
            idx = i + questions[i][1] + 1

            if idx < n:
                dp[i] += dp[idx]
            dp[i] = max(dp[i],dp[i+1])

        return dp[0]                   
        