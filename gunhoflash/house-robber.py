from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    answerPrevPrev = answerPrev = answerNow = 0

    for num in nums:
      answerNow = max(answerPrevPrev + num, answerPrev)
      answerPrevPrev = answerPrev
      answerPrev = answerNow

    return max(answerNow, answerPrev)
