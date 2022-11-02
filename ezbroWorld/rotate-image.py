from copy import deepcopy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        matrixCopy = deepcopy(matrix)
        
        for i in range(length) : 
            for j in range(length) : 
                matrix[j][length-1-i] = matrixCopy[i][j]
                
                
                
        # 10 11 12  -> 01 11 21 
        
        #  x  x  x     x  4  x
        #  4  5  6     x  5  x
        #  x  x  x     x  6  x
