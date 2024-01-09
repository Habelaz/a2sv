class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []  # Use a set to store unique triplets
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    result.append((nums[i], nums[j], nums[k]))
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                        
        return result
