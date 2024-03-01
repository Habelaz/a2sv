class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        def comb(num):
            if sum(path) == target and path not in ans:
                ans.append(path[:])
            elif sum(path) > target:
                return
            
            for i in range(num,len(candidates)):
                path.append(candidates[i])
                comb(i)
                comb(i+1)
                path.pop()
        comb(0)
        return ans
