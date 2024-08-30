class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lessThan = 0
        strictlyLess = 0

        for n in nums:
            if n <= target:
                lessThan += 1
            if n < target:
                strictlyLess += 1

        return list(range(strictlyLess,lessThan))
        
