class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        max_score = 0
        max_indices = []
        count_zeroes = 0
        count_ones = nums.count(1)
        
        for i in range(len(nums) + 1):
            score = count_zeroes + (count_ones if i < len(nums) else 0)
            if score > max_score:
                max_score = score
                max_indices = [i]
            elif score == max_score:
                max_indices.append(i)
            
            
            if i < len(nums) and nums[i] == 0:
                count_zeroes += 1
            
            if i < len(nums) and nums[i] == 1:
                count_ones -= 1
        
        return max_indices