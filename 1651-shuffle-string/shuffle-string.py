class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # random = list(s)
        # for i in range(len(s)):
        #     x = indices[i]
        #     random[i] = s[x]
        # shuffled = ''.join(random)
        # return shuffled
        shuffled = [None] * len(s)
        for i,c in enumerate(s):
            shuffled[indices[i]] = c
        return ''.join(shuffled)


