class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        @cache
        def dp(i):
            if i >= len(days):
                return 0
            min_cost = float('inf')
            for pas,cost in zip((1,7,30),costs):
                temp = i

                while temp < len(days) and days[temp] < days[i] + pas:
                    temp += 1

                min_cost = min(min_cost,cost+dp(temp))
            return min_cost

        return dp(0)