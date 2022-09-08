from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    nIsland = 0
    nRow = len(grid)
    nCol = len(grid[0])

    for row in range(nRow):
      for col in range(nCol):
        if grid[row][col] == '0': continue

        nIsland += 1

        grid[row][col] = '0'
        visitingStack = [(row, col)]

        while len(visitingStack):
          (r, c) = visitingStack.pop()
          if r > 0 and grid[r - 1][c] == '1':
            grid[r - 1][c] = '0'
            visitingStack.append((r - 1, c))
          if c > 0 and grid[r][c - 1] == '1':
            grid[r][c - 1] = '0'
            visitingStack.append((r, c - 1))
          if c < nCol - 1 and grid[r][c + 1] == '1':
            grid[r][c + 1] = '0'
            visitingStack.append((r, c + 1))
          if r < nRow - 1 and grid[r + 1][c] == '1':
            grid[r + 1][c] = '0'
            visitingStack.append((r + 1, c))

    return nIsland
