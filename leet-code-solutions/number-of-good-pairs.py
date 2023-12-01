class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_counts = {}
        good_pairs = 0

        for num in nums:
            if num in num_counts:
                good_pairs += num_counts[num]
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        return good_pairs

                