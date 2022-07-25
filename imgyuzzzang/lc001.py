# 1. Two Sum
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
    return []


print(twoSum([2,7,11,15], 9))