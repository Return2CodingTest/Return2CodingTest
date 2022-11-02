function setZeroes(matrix: number[][]): void {
  const R = matrix.length;
  const C = matrix[0].length;

  // flags for first row and col
  let isFirstRowZero = false;
  let isFirstColZero = false;

  // set flags
  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      if (matrix[r][c] === 0) {
        matrix[r][0] = matrix[0][c] = 0;
        if (r === 0) {
          isFirstRowZero = true;
        }
        if (c === 0) {
          isFirstColZero = true;
        }
      }
    }
  }

  // set zeros except first row and col
  for (let r = 1; r < R; r++) {
    for (let c = 1; c < C; c++) {
      if (matrix[r][0] === 0 || matrix[0][c] === 0) {
        matrix[r][c] = 0;
      }
    }
  }

  // set zeros at first row and col
  if (isFirstRowZero) {
    for (let c = 0; c < C; c++) {
      matrix[0][c] = 0;
    }
  }
  if (isFirstColZero) {
    for (let r = 0; r < R; r++) {
      matrix[r][0] = 0;
    }
  }
}
