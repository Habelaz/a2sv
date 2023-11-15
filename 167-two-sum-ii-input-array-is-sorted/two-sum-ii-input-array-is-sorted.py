class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index=[]
        n=len(numbers)
        l,r = 0 , n - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                index = [l+1,r+1]
                # return index
                break
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return index
