class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map1 = Counter(p)
        l = 0
        k = len(p)
        ans = []
        for r in range(k,len(s)+1):
            wind = s[l:r]
            map2 = Counter(wind)
            if map1 == map2:
                ans.append(l)
                print(l)
            l += 1
        return ans