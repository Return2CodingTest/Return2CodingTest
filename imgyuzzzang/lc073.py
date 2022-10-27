class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_row = len(matrix)
        n_col = len(matrix[0])
        zero_cols = set()
        zero_rows = set()
        
        for row in range(n_row):
            for col in range(n_col):
                if matrix[row][col] == 0:
                    zero_cols.add(col)
                    zero_rows.add(row)
        
        for row in range(n_row):
            for col in range(n_col):
                if col in zero_cols or row in zero_rows:
                    matrix[row][col] = 0        
        