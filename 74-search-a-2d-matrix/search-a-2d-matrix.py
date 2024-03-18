class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = []
        for i in range(len(matrix)):
            li += matrix[i]
        
        low,high = 0,len(li) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # print(mid)
            if li[mid] == target:
                return True
            elif li[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return li[low % len(li)] == target