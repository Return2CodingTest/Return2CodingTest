function exist(board: string[][], word: string): boolean {
  const R = board.length;
  const C = board[0].length;
  const L = word.length;

  function searchNextChar(i: number, r: number, c: number) {
    if (board[r][c] !== word[i]) return false;
    if (i + 1 === L) return true;
    board[r][c] = '';
    let result: Boolean = (
      (r > 0 && searchNextChar(i + 1, r - 1, c)) ||
      (r < R - 1 && searchNextChar(i + 1, r + 1, c)) ||
      (c > 0 && searchNextChar(i + 1, r, c - 1)) ||
      (c < C - 1 && searchNextChar(i + 1, r, c + 1))
    );
    board[r][c] = word[i];
    return result;
  }

  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      if (searchNextChar(0, r, c)) {
        return true;
      }
    }
  }
  return false;
}
