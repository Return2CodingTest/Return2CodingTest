from typing import List

class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    R = len(matrix)
    C = len(matrix[0])

    # flags for first row and col
    isFirstRowZero = False
    isFirstColZero = False

    # set flags
    for r in range(R):
      for c in range(C):
        if matrix[r][c] == 0:
          matrix[r][0] = 0
          matrix[0][c] = 0
          if r == 0:
            isFirstRowZero = True
          if c == 0:
            isFirstColZero = True

    # set zeros except first row and col
    for r in range(1, R):
      for c in range(1, C):
        if matrix[r][0] == 0 or matrix[0][c] == 0:
          matrix[r][c] = 0

    # set zeros at first row and col
    if isFirstRowZero:
      for c in range(C):
        matrix[0][c] = 0
    if isFirstColZero:
      for r in range(R):
        matrix[r][0] = 0
