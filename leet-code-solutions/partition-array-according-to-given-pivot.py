class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l ,r = 0 ,len(nums) - 1
        less=[]
        greater=[]
        equal = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            elif i == pivot:
                equal.append(i)
        return less+equal+greater

