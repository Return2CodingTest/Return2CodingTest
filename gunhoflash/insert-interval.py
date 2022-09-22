from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    minNum = min(intervals[0][0], newInterval[0]) if len(intervals) else newInterval[0]
    maxNum = max(intervals[-1][1], newInterval[1]) if len(intervals) else newInterval[1]

    # init up-down counts
    upCounts = [0] * (maxNum + 1)
    downCounts = [0] * (maxNum + 1)
    upCounts[newInterval[0]] = 1
    downCounts[newInterval[1]] = 1
    for [start, end] in intervals:
      upCounts[start] += 1
      downCounts[end] += 1

    answer = []
    start = end = upDownCount = 0
    for i in range(minNum, maxNum + 1):
      up = upCounts[i]
      down = downCounts[i]

      if up != 0 and upDownCount == 0:
        start = i

      upDownCount += up - down

      if down != 0 and upDownCount == 0:
        end = i
        answer.append([start, end])

    return answer
