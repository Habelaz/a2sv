class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        mapp = defaultdict(lambda :0)
        ans = [0] * len(temperatures)
        for ind,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                lower = stack.pop()
                # print(lower)
                # mapp[lower] = temp
                ans[lower] = ind - lower
            stack.append(ind)

        return ans