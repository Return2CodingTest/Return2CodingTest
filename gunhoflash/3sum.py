from typing import List

class Solution:
  def threeSum(self, _nums: List[int]) -> List[List[int]]:
    nums = _nums[:]
    nums.sort()

    nNumMap = {}
    for num in nums:
      nNumMap[num] = nNumMap.get(num, 0) + 1

    answer = []
    prevNum1 = None
    for i, num in enumerate(nums):
      num1 = num
      if num1 == prevNum1: continue
      prevNum1 = num1

      prevNum2 = None
      for j in range(i + 1, len(nums)):
        num2 = nums[j]
        if num2 == prevNum2: continue
        prevNum2 = num2

        target = (num1 + num2) * -1
        if target < num2: continue

        nTarget = nNumMap.get(target, 0) \
           - (1 if num1 == target else 0) \
           - (1 if num2 == target else 0)
        if nTarget > 0:
          answer.append([num1, num2, target])

    return answer
