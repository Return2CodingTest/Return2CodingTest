class Solution:
  def climbStairs(self, n: int) -> int:
    prevPrevStep = 0
    prevStep = 1
    step = 0

    while n:
      n -= 1
      step = prevPrevStep + prevStep
      prevPrevStep = prevStep
      prevStep = step

    return step
