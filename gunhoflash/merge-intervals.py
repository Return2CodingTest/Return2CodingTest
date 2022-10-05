from typing import List

MAX_VALUE = 10000

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # init up-down counts
    upCounts = [0] * (MAX_VALUE + 1)
    downCounts = [0] * (MAX_VALUE + 1)
    for [start, end] in intervals:
      upCounts[start] += 1
      downCounts[end] += 1

    answer = []
    start = end = upDownCount = 0
    for i in range(0, 10001):
      up = upCounts[i]
      down = downCounts[i]

      if up != 0 and upDownCount == 0:
        start = i

      upDownCount += up - down

      if down != 0 and upDownCount == 0:
        end = i
        answer.append([start, end])

    return answer
