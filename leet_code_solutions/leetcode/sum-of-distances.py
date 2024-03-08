class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)

        for i, n in enumerate(nums):
            d[n].append(i)
        
        res = [0] * len(nums)
        for n in d:
            l = d[n]
            pref = [0]
            for x in l:
                pref.append(pref[-1] + x)
            for i, x in enumerate(l):
                left = x * (i + 1) - pref[i + 1]
                right = pref[-1] - pref[i] - x * (len(l) - i)
                res[x] = left + right
        
        return res
            