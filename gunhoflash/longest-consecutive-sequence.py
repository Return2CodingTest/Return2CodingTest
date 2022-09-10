from typing import List

class Element:
  def __init__(self, value, left, right):
    self.value = value
    self.left = left if left else self
    self.right = right if right else self

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    answer = 0
    m = {}

    for num in nums:
      # skip if already exists
      if m.get(num): continue

      # find left and right elements
      left = m.get(num - 1)
      if left:
        left = left.left

      right = m.get(num + 1)
      if right:
        right = right.right

      # create new element with value num
      element = Element(num, left, right)
      m[num] = element

      # update left and right elements
      element.left.right = element.right
      element.right.left = element.left

      # update answer
      answer = max(answer, element.right.value - element.left.value + 1)

    return answer
