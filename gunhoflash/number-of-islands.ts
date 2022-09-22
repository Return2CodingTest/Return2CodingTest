function numIslands(grid: string[][]): number {
  let nIsland = 0;
  const nRow = grid.length;
  const nCol = grid[0].length;

  const isIsland = (r: number, c: number) =>  0 <= r && r < nRow && 0 <= c && c < nCol && grid[r][c] === '1';

  const clearLand = (r: number, c: number) => grid[r][c] = '0';

  for (let row = 0; row < nRow; ++row) {
    for (let col = 0; col < nCol; ++col) {
      if (!isIsland(row, col)) continue;

      ++nIsland;

      clearLand(row, col);
      const visitingStack = [[row, col]];

      while (visitingStack.length) {
        const [r, c] = visitingStack.pop()!;
        if (isIsland(r - 1, c)) {
          clearLand(r - 1, c);
          visitingStack.push([r - 1, c]);
        }
        if (isIsland(r, c - 1)) {
          clearLand(r, c - 1);
          visitingStack.push([r, c - 1]);
        }
        if (isIsland(r, c + 1)) {
          clearLand(r, c + 1);
          visitingStack.push([r, c + 1]);
        }
        if (isIsland(r + 1, c)) {
          clearLand(r + 1, c);
          visitingStack.push([r + 1, c]);
        }
      }
    }
  }

  return nIsland;
}
