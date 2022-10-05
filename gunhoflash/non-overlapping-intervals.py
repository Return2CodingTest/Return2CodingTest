from typing import List

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    sortedIntervalList = sorted(intervals)
    nowEnd = -50000
    nDeleted = 0

    for [start, end] in sortedIntervalList:
      if nowEnd <= start:
        # not overlapped
        nowEnd = end
        continue

      # overlapped
      nDeleted += 1
      if end < nowEnd:
        nowEnd = end

    return nDeleted
