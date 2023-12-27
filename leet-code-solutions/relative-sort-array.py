class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sortedd = []

        for num in arr2:
            while num in arr1:
                sortedd.append(num)
                arr1.remove(num)
        arr1.sort()
        ans = sortedd + arr1
        return ans
        
        