from typing import List

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    answer = max(nums)

    minPositiveSerialProduct = 1
    maxNegativeSerialProduct = 0
    serialProduct = 1

    for num in nums:
      serialProduct *= num

      if serialProduct < 0:
        if maxNegativeSerialProduct == 0:
          maxNegativeSerialProduct = serialProduct
        else:
          answer = max(answer, serialProduct // maxNegativeSerialProduct)
          maxNegativeSerialProduct = max(maxNegativeSerialProduct, serialProduct)
      elif serialProduct > 0:
        answer = max(answer, serialProduct // minPositiveSerialProduct)
        minPositiveSerialProduct = min(minPositiveSerialProduct, serialProduct)
      else:
        minPositiveSerialProduct = 1
        maxNegativeSerialProduct = 0
        serialProduct = 1

    return answer
