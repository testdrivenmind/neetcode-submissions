class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        self.sum_matrix = [[0] * cols for row in range(rows)] 
        for row in range(rows):
            for col in range(cols):
                left = self.sum_matrix[row][col-1] if col > 0 else 0
                up = self.sum_matrix[row-1][col] if row > 0 else 0
                diagonal = self.sum_matrix[row-1][col-1] if row > 0 and col > 0 else 0
                self.sum_matrix[row][col] = self.matrix[row][col] + left + up - diagonal  
                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.total_sum = self.sum_matrix[row2][col2]
        self.up_sum = self.sum_matrix[row1-1][col2] if row1 > 0 else 0
        self.left_sum = self.sum_matrix[row2][col1-1] if col1 > 0 else 0
        self.overlap_sum = self.sum_matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self.total_sum - self.up_sum - self.left_sum + self.overlap_sum
    


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)