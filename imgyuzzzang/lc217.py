# 217. Contains Duplicate
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    numSet = set(nums)
    return len(nums) != len(numSet)

print(containsDuplicate([1,2,3,1]))