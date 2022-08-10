from typing import List

class Solution:
  def maxArea(self, heights: List[int]) -> int:
    answer = 0
    leftIndex = 0
    rightIndex = len(heights) - 1

    while leftIndex < rightIndex:
      leftHeight = heights[leftIndex]
      rightHeight = heights[rightIndex]

      area = (rightIndex - leftIndex) * min(leftHeight, rightHeight)
      answer = max(answer, area)

      if rightHeight > leftHeight:
        leftIndex += 1
      else:
        rightIndex -= 1

    return answer
