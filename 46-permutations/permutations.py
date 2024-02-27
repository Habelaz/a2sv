class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def permute(n):

            if len(nums) == len(path):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    permute(i+1)
                    path.pop()
        permute(0)
        return ans

                