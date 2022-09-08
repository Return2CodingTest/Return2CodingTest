from typing import List

class Cell:
  def __init__(self):
    self.pacific = False
    self.atlantic = False

class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    nRow = len(heights)
    nCol = len(heights[0])

    # [flow to Pacific, flow to Atlantic] 행렬
    cells = [[Cell() for _ in range(nCol)] for _ in range(nRow)]

    # 가장자리 셀 설정
    for row in range(nRow):
      cells[row][0].pacific = True
      cells[row][nCol - 1].atlantic = True
    for col in range(nCol):
      cells[0][col].pacific = True
      cells[nRow - 1][col].atlantic = True

    # 모든 셀에 대해, bool 전파 (전파 중 이미 전파된 셀을 만나면 해당셀은 스킵)
    for row in range(nRow):
      for col in range(nCol):
        # 전파할 정보
        pacific = cells[row][col].pacific
        atlantic = cells[row][col].atlantic

        # 전파할 것이 없음: 스킵
        if not pacific and not atlantic: continue

        visitingStack = [(row, col)]
        while len(visitingStack):
          (r, c) = visitingStack.pop()
          height = heights[r][c]
          # 높이 비교, 새로 전파할 정보가 있는지 확인 후 전파
          if r > 0 and heights[r - 1][c] >= height and ((pacific and not cells[r - 1][c].pacific) or (atlantic and not cells[r - 1][c].atlantic)):
            cells[r - 1][c].pacific |= pacific
            cells[r - 1][c].atlantic |= atlantic
            visitingStack.append((r - 1, c))
          if c > 0 and heights[r][c - 1] >= height and ((pacific and not cells[r][c - 1].pacific) or (atlantic and not cells[r][c - 1].atlantic)):
            cells[r][c - 1].pacific |= pacific
            cells[r][c - 1].atlantic |= atlantic
            visitingStack.append((r, c - 1))
          if r < nRow - 1 and heights[r + 1][c] >= height and ((pacific and not cells[r + 1][c].pacific) or (atlantic and not cells[r + 1][c].atlantic)):
            cells[r + 1][c].pacific |= pacific
            cells[r + 1][c].atlantic |= atlantic
            visitingStack.append((r + 1, c))
          if c < nCol - 1 and heights[r][c + 1] >= height and ((pacific and not cells[r][c + 1].pacific) or (atlantic and not cells[r][c + 1].atlantic)):
            cells[r][c + 1].pacific |= pacific
            cells[r][c + 1].atlantic |= atlantic
            visitingStack.append((r, c + 1))

    # [flow to Pacific, flow to Atlantic] 가 모두 True인 셀만 필터링
    answer = []
    for row in range(nRow):
      for col in range(nCol):
        if cells[row][col].atlantic and cells[row][col].pacific:
          answer.append([row, col])

    return answer
