class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt2 = Counter()
        for word in words2:
            w = Counter(word)
            for c, f in w.items():
                cnt2[c] = max(cnt2[c], f) 

        ans = []
        for w in words1:
            cnt1 = Counter(w)
            subset = True
            for key,val in cnt2.items():
                # print(key,cnt1[key])
                if cnt1[key] < val:
                    subset = False
                    break
            if subset:
                ans.append(w)
        return ans