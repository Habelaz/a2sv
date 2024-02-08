class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_l = [trips[i][-1] for i in range(len(trips))]
        n = max(max_l)
        pref = [0] * (n+1)

        for i in range(len(trips)):
            peoples = trips[i][0]
            start = trips[i][1]
            end = trips[i][-1]

            pref[start] += peoples
            pref[end] -= peoples

        for i in range(1,len(pref)):
            pref[i] += pref[i-1]
        
        for n in pref:
            if n > capacity:
                return False
        else:
            return True