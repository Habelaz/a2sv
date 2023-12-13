class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        in_both = set()
        
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                in_both.add(fronts[i])

        ans = float('inf')

        for i in range(len(fronts)):
            if fronts[i] not in in_both:
                ans = min(ans, fronts[i])
            if backs[i] not in in_both:
                ans = min(ans, backs[i])

        return ans if ans != float('inf') else 0