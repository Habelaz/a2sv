class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for ind,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                lower = stack.pop()
                ans[lower] = ind - lower
            
            stack.append(ind)
        return ans
        