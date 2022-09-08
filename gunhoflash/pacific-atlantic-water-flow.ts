class Cell {
  pacific: boolean;
  atlantic: boolean;

  constructor() {
    this.pacific = false;
    this.atlantic = false;
  }
}

function pacificAtlantic(heights: number[][]): number[][] {
  const nRow = heights.length;
  const nCol = heights[0].length;

  // [flow to Pacific, flow to Atlantic] 행렬
  const cells = Array(nRow).fill(null).map(() => Array(nCol).fill(null).map(() => new Cell()));

  // 가장자리 셀 설정
  for (let row = 0; row < nRow; ++row) {
    cells[row][0].pacific = true;
    cells[row][nCol - 1].atlantic = true;
  }
  for (let col = 0; col < nCol; ++col) {
    cells[0][col].pacific = true;
    cells[nRow - 1][col].atlantic = true;
  }

  // 모든 셀에 대해, bool 전파 (전파 중 이미 전파된 셀을 만나면 해당셀은 스킵)
  for (let row = 0; row < nRow; ++row) {
    for (let col = 0; col < nCol; ++col) {
      // 전파할 정보
      const {pacific, atlantic} = cells[row][col];

      // 전파할 것이 없음: 스킵
      if (!pacific && !atlantic) continue;

      const visitingStack = [[row, col]];
      while (visitingStack.length) {
        const [r, c] = visitingStack.pop()!;
        const height = heights[r][c];
        // 높이 비교, 새로 전파할 정보가 있는지 확인 후 전파
        if (r > 0 && heights[r - 1][c] >= height && ((pacific && !cells[r - 1][c].pacific) || (atlantic && !cells[r - 1][c].atlantic))) {
          cells[r - 1][c].pacific ||= pacific;
          cells[r - 1][c].atlantic ||= atlantic;
          visitingStack.push([r - 1, c]);
        }
        if (c > 0 && heights[r][c - 1] >= height && ((pacific && !cells[r][c - 1].pacific) || (atlantic && !cells[r][c - 1].atlantic))) {
          cells[r][c - 1].pacific ||= pacific;
          cells[r][c - 1].atlantic ||= atlantic;
          visitingStack.push([r, c - 1]);
        }
        if (r < nRow - 1 && heights[r + 1][c] >= height && ((pacific && !cells[r + 1][c].pacific) || (atlantic && !cells[r + 1][c].atlantic))) {
          cells[r + 1][c].pacific ||= pacific;
          cells[r + 1][c].atlantic ||= atlantic;
          visitingStack.push([r + 1, c]);
        }
        if (c < nCol - 1 && heights[r][c + 1] >= height && ((pacific && !cells[r][c + 1].pacific) || (atlantic && !cells[r][c + 1].atlantic))) {
          cells[r][c + 1].pacific ||= pacific;
          cells[r][c + 1].atlantic ||= atlantic;
          visitingStack.push([r, c + 1]);
        }
      }
    }
  }

  // [flow to Pacific, flow to Atlantic] 가 모두 True인 셀만 필터링
  const answer: [number, number][] = [];
  for (let row = 0; row < nRow; ++row) {
    for (let col = 0; col < nCol; ++col) {
      if (cells[row][col].atlantic && cells[row][col].pacific) {
        answer.push([row, col]);
      }
    }
  }

  return answer;
}
