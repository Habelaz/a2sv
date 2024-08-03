class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []

        for i,n in enumerate(nums):
            n = str(n)
            mapped_num = 0
            for c in n:
                mapped_num *= 10
                mapped_num += mapping[int(c)]
            
            arr.append((mapped_num,i))
        
        arr.sort()
        # print(arr)
        return [nums[p[1]] for p in arr]
            