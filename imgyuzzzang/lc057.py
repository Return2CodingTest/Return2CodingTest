#57. Insert Interval

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    
    if n == 0:
        return [newInterval]
    
    maxNum = max(intervals[n-1][1], newInterval[1]) 
    minNum = min(intervals[0][0],newInterval[0])
    dots = [0] * (maxNum + 2)
    fill = [0] * (maxNum + 2)
    res = []

    def fillInterval (start, end):
        if start == end:
            dots[start] = 1
        for i in range(start, end):
            fill[i] = 1
    
    for start, end in intervals:
        fillInterval(start, end)  
    
    fillInterval(newInterval[0], newInterval[1])
        
    start = end = 0
    
    for i in range(minNum-1, maxNum+1):
        if fill[i] == 0 and  fill[i+1] == 1:
            start = i+1
        if fill[i] == 1 and  fill[i+1] == 0:
            end = i+1
            res.append([start, end])
        if dots[i+1] == 1 and fill[i] != 1 and fill[i+1] != 1:
            res.append([i+1,i+1])
            
    return res