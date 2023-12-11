class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_dict = {num: i for i, num in enumerate(nums)}

        for k, j in operations:
            x = my_dict[k]
            nums[x] = j
            my_dict[j] = x
            del my_dict[k]

        return nums