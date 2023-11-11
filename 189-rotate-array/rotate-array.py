class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums) - 1
        for i in range(k):
            x = nums.pop()
            nums.insert(0,x)
