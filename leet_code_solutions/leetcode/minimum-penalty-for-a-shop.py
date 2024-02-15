class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pref = [0] *(len(customers)+1)

        for i in range(len(customers)):
            if customers[i] == 'N':
                pref[i] += 1
        
        acc = 0
        neww =pref.copy()
        for i in range(len(pref)):
            pref[i] = acc
            acc += neww[i]
        # print(pref)
        suff = [0] *(len(pref))
        for i in range(len(customers)):
            if customers[i] == 'Y':
                suff[i] += 1
        # print(suff)
        acc = 0
        
        for i in range(len(pref)-1,-1,-1):
            suff[i] += acc
            acc = suff[i]
            pref[i] += suff[i]
        x = min(pref)
        ind = pref.index(x)
        return ind
