class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pref = [[0 for i in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)] 
        
        for i in range(len(matrix)+1):
            for j in range(len(matrix[0])+1):
                 self.pref[i][j] = self.pref[i-1][j] + self.pref[i][j-1] - self.pref[i-1][j-1] + matrix[i-1][j-1] 
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        sub_sum = self.pref[row2+1][col2+1] - self.pref[row2+1][col1] - self.pref[row1][col2+1] + self.pref[row1][col1]
        return sub_sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)