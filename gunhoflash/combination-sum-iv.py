from typing import List

class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    answers = [0] * (target + 1)
    answers[0] = 1

    for i in range(target + 1):
      for num in nums:
        if num <= i:
          answers[i] += answers[i - num]

    return answers[target]
