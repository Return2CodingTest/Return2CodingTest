function numIslands(grid: string[][]): number {
  let nIsland = 0;
  const nRow = grid.length;
  const nCol = grid[0].length;

  for (let row = 0; row < nRow; ++row) {
    for (let col = 0; col < nCol; ++col) {
      if (grid[row][col] === '0') continue;

      ++nIsland;

      grid[row][col] = '0';
      const visitingStack = [[row, col]];

      while (visitingStack.length) {
        const [r, c] = visitingStack.pop()!;
        if (r > 0 && grid[r - 1][c] === '1') {
          grid[r - 1][c] = '0';
          visitingStack.push([r - 1, c]);
        }
        if (c > 0 && grid[r][c - 1] === '1') {
          grid[r][c - 1] = '0';
          visitingStack.push([r, c - 1]);
        }
        if (c < nCol - 1 && grid[r][c + 1] === '1') {
          grid[r][c + 1] = '0';
          visitingStack.push([r, c + 1]);
        }
        if (r < nRow - 1 && grid[r + 1][c] === '1') {
          grid[r + 1][c] = '0';
          visitingStack.push([r + 1, c]);
        }
      }
    }
  }

  return nIsland;
}
