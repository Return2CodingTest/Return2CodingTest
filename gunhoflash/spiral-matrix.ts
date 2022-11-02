function spiralOrder(matrix: number[][]): number[] {
  let startRow = 0;
  let endRow = matrix.length - 1;
  let startCol = 0;
  let endCol = matrix[0].length - 1;

  const answer = Array((endRow - startRow + 1) * (endCol - startCol + 1)).fill(0);
  let i = 0;
  while (startRow <= endRow && startCol <= endCol) {
    if (startRow === endRow) {
      for (let col = startCol; col <= endCol; col++) {
        answer[i++] = matrix[startRow][col];
      }
      break;
    }
    if (startCol === endCol) {
      for (let row = startRow; row <= endRow; row++) {
        answer[i++] = matrix[row][endCol];
      }
      break;
    }
    for (let col = startCol; col < endCol; col++) {
      answer[i++] = matrix[startRow][col];
    }
    for (let row = startRow; row < endRow; row++) {
      answer[i++] = matrix[row][endCol];
    }
    for (let col = endCol; col > startCol; col--) {
      answer[i++] = matrix[endRow][col];
    }
    for (let row = endRow; row > startRow; row--) {
      answer[i++] = matrix[row][startCol];
    }
    startRow++;
    endRow--;
    startCol++;
    endCol--;
  }

  return answer;
}
