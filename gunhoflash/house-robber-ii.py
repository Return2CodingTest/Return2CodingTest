from typing import List

class Solution:
  def robLinear(self, nums: List[int]) -> int:
    answerPrevPrev = answerPrev = answerNow = 0

    for num in nums:
      answerNow = max(answerPrevPrev + num, answerPrev)
      answerPrevPrev = answerPrev
      answerPrev = answerNow

    return max(answerNow, answerPrev)

  def rob(self, nums: List[int]) -> int:
    # 첫 집을 턴다면: 마지막 집은 못 터므로 이를 제거하고 선형으로 풀이한다.
    # 첫 집을 안 턴다면: 첫 집을 제거하고 선형으로 풀이한다.
    # 예외: 집이 하나 뿐이라면 위 방법을 사용하지 말아야 한다.

    if len(nums) <= 2:
      return max(nums)

    return max(self.robLinear(nums[:-1]), self.robLinear(nums[1:]))
