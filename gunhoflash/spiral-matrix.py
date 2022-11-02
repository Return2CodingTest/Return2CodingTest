from typing import List

class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    startRow = 0
    endRow = len(matrix) - 1
    startCol = 0
    endCol = len(matrix[0]) - 1

    answer = []
    while startRow <= endRow and startCol <= endCol:
      if startRow == endRow:
        for col in range(startCol, endCol + 1):
          answer.append(matrix[startRow][col])
        break
      if startCol == endCol:
        for row in range(startRow, endRow + 1):
          answer.append(matrix[row][endCol])
        break
      for col in range(startCol, endCol):
        answer.append(matrix[startRow][col])
      for row in range(startRow, endRow):
        answer.append(matrix[row][endCol])
      for col in range(endCol, startCol, -1):
        answer.append(matrix[endRow][col])
      for row in range(endRow, startRow, -1):
        answer.append(matrix[row][startCol])
      startRow += 1
      endRow -= 1
      startCol += 1
      endCol -= 1

    return answer
