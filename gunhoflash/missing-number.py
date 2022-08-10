from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    max = len(nums)
    return (max * (max + 1) // 2) - sum(nums)
