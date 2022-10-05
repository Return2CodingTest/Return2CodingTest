from typing import List

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    # obviously, the last index is reachable to itself
    closestReachableIndex = len(nums) - 1

    # search reachable indexes from last index to start index
    for i, num in reversed(list(enumerate(nums))):
      if i + num >= closestReachableIndex:
        closestReachableIndex = i

    return closestReachableIndex == 0
