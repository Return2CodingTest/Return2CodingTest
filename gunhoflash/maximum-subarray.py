from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    sumFromStart = 0
    minSum = 0
    maxSum = nums[0]

    for num in nums:
      sumFromStart += num
      maxSum = max(maxSum, sumFromStart - minSum)
      minSum = min(minSum, sumFromStart)

    return maxSum
