class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r = 0 ,len(skill) - 1
        target= skill[l]+skill[r]
        ans=0
        while l < r:
            if skill[l]+skill[r] == target:
                ans += (skill[l]*skill[r])
            elif skill[l]+skill[r] > target or skill[l]+skill[r] < target:
                return -1
            l += 1
            r -= 1
        return ans