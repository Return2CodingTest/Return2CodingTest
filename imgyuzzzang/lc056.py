#56. Merge Intervals

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    intervals.sort()
    res = []
    start, end = intervals[0]
    for i in range(1,n):
        nextStart, nextEnd = intervals[i]
        if end >= nextStart:
            end = max(nextEnd, end)
        else:
            res.append([start, end])
            start, end = nextStart, nextEnd
            
    res.append([start,end])
    
    return res