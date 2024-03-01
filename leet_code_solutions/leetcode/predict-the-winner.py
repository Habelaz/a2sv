class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def predict(left, right):
            if left == right:
                return nums[right]

            left_side = nums[left] - predict(left + 1, right)
            right_side = nums[right] - predict(left, right - 1)

            return max(left_side, right_side)
        
        return predict(0, len(nums) - 1) >= 0
        