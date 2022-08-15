# 11. Container With Most Water

from typing import List

def maxArea(height: List[int]) -> int:
    n = len(height)
    start = 0
    end = n-1

    def getMax():
        return min(height[start], height[end]) * (end - start)

    res = 0 

    while(start < end):
        res = max(getMax(), res)
        print(res)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
        print(start, end)

    return res

print(maxArea([1,1]))