class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        l, r = 0, 1

        while r < len(arr) and arr[l] < arr[r]:
            l += 1
            r += 1

        if r == 1 or r == len(arr):
            return False

        while r < len(arr) and arr[l] > arr[r]:
            l += 1
            r += 1

        return r == len(arr)