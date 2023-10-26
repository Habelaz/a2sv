class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index=[]
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            if numbers[i]+numbers[j] == target:
                index=[i+1,j+1]
                break
            elif numbers[i]+numbers[j] > target:
                j -= 1
            else:
                i += 1
        return index