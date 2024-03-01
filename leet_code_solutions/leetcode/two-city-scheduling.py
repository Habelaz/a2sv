class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = sorted(costs, key = lambda x: x[0] - x[1])
        ans = 0
        n = len(costs)
        for i in range(n):
            if i < n //2:
                ans += a[i][0]

            else:
                ans += a[i][1]
        return ans