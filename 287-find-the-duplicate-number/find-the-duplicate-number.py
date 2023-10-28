class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        alre=set()
        for i in nums:
            if i in alre:
                return i
            alre.add(i)