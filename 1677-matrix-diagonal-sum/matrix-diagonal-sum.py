class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j == len(mat) - 1:
                    count += mat[i][j]
                if i == j:
                    count += mat[i][j]
        if len(mat) % 2 :
            row = len(mat)//2
            col = row
            count -= mat[row][col]
        return count