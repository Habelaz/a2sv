class Solution:
    def maximumLength(self, s: str) -> int:
        mapp = defaultdict(int)

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                w = s[i:j]
                mapp[w] += 1
        # print(mapp)
        # return 0                
        ans = -1
        for key,val in mapp.items():
            if val >= 3 and len(set(key)) == 1:
                ans = max(ans,len(key))
        return ans
