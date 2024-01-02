class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips=[]
        for target in range(len(arr), 0, -1):
            idx = arr.index(target)
            if idx == target - 1:
                continue
            k = idx + 1
            arr[:k] = reversed(arr[:k])
            flips.append(k)
            arr[:target] = reversed(arr[:target])
            flips.append(target)

        return flips