from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    lenNums = len(nums)
    answer = [1] * lenNums

    serialProduct = 1
    for i in range(lenNums):
      answer[i] *= serialProduct
      serialProduct *= nums[i]

    serialProduct = 1
    for i in range(lenNums - 1, -1, -1):
      answer[i] *= serialProduct
      serialProduct *= nums[i]

    return answer
