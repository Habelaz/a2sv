class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if  len(nums) < 3:
            return False

        min_value = float('inf')
        second_min_value = float('inf')

        for num in nums:
            if num <= min_value:
                min_value = num
            elif num <= second_min_value:
                second_min_value = num
            else:
                return True

        return False
