class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        for i in range(len(arr)):
            arr[i] = (abs(arr[i] - x),arr[i])

        heapify(arr)
        # print(arr)
        ans = []
        for i in range(k):
            ans.append(heappop(arr)[1])
        return sorted(ans)