class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)/3
        for i in nums:
            if nums.count(i) > n:
                if i not in ans:
                    ans.append(i)
        return ans