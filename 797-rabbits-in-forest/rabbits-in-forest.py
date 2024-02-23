class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mapp = {}
        count = 0

        for ans in answers:
            if ans == 0:
                count += 1
            else:
                if ans not in mapp or mapp[ans] == ans:
                    mapp[ans] = 0
                    count += (1+ans)
                else:
                    mapp[ans] += 1
        return count