from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    nIsland = 0
    nRow = len(grid)
    nCol = len(grid[0])

    def isIsland(r, c):
      return 0 <= r < nRow and 0 <= c < nCol and grid[r][c] == '1'
    
    def clearLand(r, c):
      grid[r][c] = '0'

    for row in range(nRow):
      for col in range(nCol):
        if not isIsland(row, col): continue

        nIsland += 1

        clearLand(row, col)
        visitingStack = [(row, col)]

        while len(visitingStack):
          (r, c) = visitingStack.pop()
          if isIsland(r - 1, c):
            clearLand(r - 1, c)
            visitingStack.append((r - 1, c))
          if isIsland(r, c - 1):
            clearLand(r, c - 1)
            visitingStack.append((r, c - 1))
          if isIsland(r, c + 1):
            clearLand(r, c + 1)
            visitingStack.append((r, c + 1))
          if isIsland(r + 1, c):
            clearLand(r + 1, c)
            visitingStack.append((r + 1, c))

    return nIsland
