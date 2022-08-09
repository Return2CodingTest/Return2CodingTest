function maxArea(heights: number[]): number {
  let answer = 0;
  let leftIndex = 0;
  let rightIndex = heights.length - 1;

  while (leftIndex < rightIndex) {
    const leftHeight = heights[leftIndex];
    const rightHeight = heights[rightIndex];

    const area = (rightIndex - leftIndex) * Math.min(leftHeight, rightHeight);
    answer = Math.max(answer, area);

    if (rightHeight > leftHeight) {
      leftIndex++;
    } else {
      rightIndex--;
    }
  }

  return answer;
}
