class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(len(arr) - 1, 0, -1):
            max_index = arr.index(max(arr[:i + 1]))
            if max_index != 0:
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
                flips.append(max_index + 1)
            arr[:i + 1] = reversed(arr[:i + 1])
            flips.append(i + 1)
        return flips