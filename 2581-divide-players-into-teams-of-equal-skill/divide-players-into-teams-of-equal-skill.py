class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        n = len(skill)
        j = n - 1
        target = skill[i] + skill[j]

        chem = []
        while i < j:
            if skill[i] + skill[j] == target:
                chem.append(skill[i] * skill[j])
                i += 1
                j -= 1
            elif skill[i] + skill[j] < target or skill[i] + skill[j] > target:
                return -1  # Total skill of teams cannot be equal
            else:
                j -= 1
        
        return sum(chem)