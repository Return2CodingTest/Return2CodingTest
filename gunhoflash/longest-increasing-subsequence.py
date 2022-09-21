import math
from typing import List

class Solution:
  def updateMinWithLowerbound(self, num, nums: List[int]):
    left = 0
    right = len(nums) - 1

    while left < right:
      midIndex = (left + right) >> 1
      midValue = nums[midIndex]

      if midValue < num:
        left = midIndex + 1
      else:
        right = midIndex

    nums[left] = num

  def lengthOfLIS(self, nums: List[int]) -> int:
    lis = [math.inf]

    for num in nums:
      if num > lis[len(lis) - 1]:
        lis.append(num)
      else:
        self.updateMinWithLowerbound(num, lis)

    return len(lis)
