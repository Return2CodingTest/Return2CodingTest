from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    leftIndex = 0
    rightIndex = len(nums) - 1

    while leftIndex < rightIndex:
      midIndex = (leftIndex + rightIndex) // 2
      leftValue = nums[leftIndex]
      midValue = nums[midIndex]
      rightValue = nums[rightIndex]

      if midValue == target: return midIndex

      if leftValue <= midValue:
        if leftValue <= target and target <= midValue:
          rightIndex = midIndex
        else:
          leftIndex = midIndex + 1
      elif midValue <= target and target <= rightValue:
        leftIndex = midIndex + 1
      else:
        rightIndex = midIndex

    return leftIndex if nums[leftIndex] == target else -1
