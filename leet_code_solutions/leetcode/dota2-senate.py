class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        r = deque([])
        d = deque([])

        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        while d and r:
            dt = d.popleft()
            rt = r.popleft()

            if rt < dt:
                r.append(rt + len(senate))
            else:
                d.append(dt + len(senate))
        if r:
            return 'Radiant'
        else:
            return 'Dire'