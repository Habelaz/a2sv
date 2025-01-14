class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        count = [0] * (len(A)+1)
        cmn = 0
        for i in range(len(A)):
            count[A[i]] += 1

            if count[A[i]] == 2:
                cmn += 1
            count[B[i]] += 1
            if count[B[i]] == 2:
                cmn += 1
            ans.append(cmn)
        return ans