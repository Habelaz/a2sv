class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if n-1 in numSet:
                continue
                
            currentSequenceSize = 1

            while (n+currentSequenceSize) in numSet:
                currentSequenceSize += 1

            longest = max(currentSequenceSize, longest)
    
        return longest



        