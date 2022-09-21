#153. Find Minimum in Rotated Sorted Array
from typing import List

def findMin(nums: List[int]) -> int:
    n = len(nums)
    ran = []
    start=nums[0]
    end=nums[-1]

    
    if start > end:
        ran = reversed(range(n))
    elif start < end:
        ran = range(n)
    else :
        return start
    for i in ran:
        if start < nums[i]:
            return start
        start = nums[i]
            