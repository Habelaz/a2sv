class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c =len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for row in zero_rows:
            for j in range(c):
                matrix[row][j] = 0

        for col in zero_cols:
            for i in range(r):
                matrix[i][col] = 0