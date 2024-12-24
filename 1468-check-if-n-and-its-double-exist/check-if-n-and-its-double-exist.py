class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            l,r = 0 ,len(arr) - 1
            while l <= r:
                mid= l + (r-l) // 2
                if mid != i and arr[mid] == arr[i] * 2:
                    return True
                elif arr[mid] < arr[i] * 2:
                    l += 1
                else:
                    r -= 1
        return False