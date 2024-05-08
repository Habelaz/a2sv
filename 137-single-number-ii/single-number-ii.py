class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        only = 0
        more = 0

        for num in nums:
            only = (only ^ num) & ~more
            more = (more ^ num) & ~only
            # print(only,more)
        return only