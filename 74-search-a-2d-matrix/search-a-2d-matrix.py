class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low,high = 0,len(matrix) - 1
        row = 0

        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                row = mid
                low = mid + 1
        
        low,high = 0,len(matrix[row]) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

