from typing import List

class Solution:
  def findMin(self, nums: List[int]) -> int:
    leftIndex = 0
    rightIndex = len(nums) - 1

    while leftIndex < rightIndex:
      midIndex = (leftIndex + rightIndex) // 2
      midValue = nums[midIndex]
      rightValue = nums[rightIndex]

      if midValue < rightValue:
        rightIndex = midIndex
      else:
        leftIndex = midIndex + 1

    return nums[leftIndex]
