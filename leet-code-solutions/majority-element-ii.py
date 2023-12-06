class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)/3

        for i in nums:
            if i not in ans:
                if nums.count(i) > n:
                    ans.append(i)
        return ans