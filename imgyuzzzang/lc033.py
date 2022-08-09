#33. Search in Rotated Sorted Array
from typing import List

def search(nums: List[int], target: int) -> int:
    n = len(nums)
    ran = range(n)
    isReversed = False
    start = nums[0]
    
    if target < start:
        ran = reversed(range(n))
        isReversed = True

    if n == 1:
        return 0 if target == start else -1
    
    for i in ran:
        if nums[i] == target:
            return i
        if (isReversed ^ (nums[i] < start)) or (isReversed ^ (nums[i] > target)):
            return -1
        start = nums[i]
    return -1

print(search([1,3],1))
print(search([1],0))
print(search([4,5,6,7,0,1,2],0))