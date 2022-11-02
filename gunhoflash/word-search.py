from typing import List

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    R = len(board)
    C = len(board[0])
    L = len(word)

    def searchNextChar(i: int, r: int, c: int) -> bool:
      if board[r][c] != word[i]: return False
      if i + 1 == L: return True
      board[r][c] = ''
      result = False
      if r > 0 and searchNextChar(i + 1, r - 1, c):
        result = True
      elif r < R - 1 and searchNextChar(i + 1, r + 1, c):
        result = True
      elif c > 0 and searchNextChar(i + 1, r, c - 1):
        result = True
      elif c < C - 1 and searchNextChar(i + 1, r, c + 1):
        result = True
      board[r][c] = word[i]
      return result

    for r in range(R):
      for c in range(C):
        if searchNextChar(0, r, c):
          return True
    return False
