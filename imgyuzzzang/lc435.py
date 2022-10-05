#435. Non-overlapping Intervals

from typing import List

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    count = 0
    intervals.sort(key = lambda x:x[1])
    
    prevEnd = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start < prevEnd:
            count += 1
        else:
            prevEnd = start
    
    return count