class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        n = len(s1)
        map1 = Counter(s1)
        l = 0
        for r in range(n,len(s2)+1):
            sub = s2[l:r]
            map2 = Counter(sub)
            print(map1,map2)
            if map1 == map2:
                return True
            l += 1
        return False
