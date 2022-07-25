# 238. Product of Array Except Self
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    res = []
    
    leftMultiple = nums[:]
    rightMultiple = nums[:]

    for i in range(1, len(nums)):
        leftMultiple[i] *= leftMultiple[i-1]
        rightMultiple[len(nums)-i-1] *= rightMultiple[len(nums)-i]
    
    for i in range(len(nums)):
        if(i == 0):
            res.append(rightMultiple[i+1])
        elif(i == len(nums)-1):
            res.append(leftMultiple[i-1])
        else:
            res.append(leftMultiple[i-1]*rightMultiple[i+1])
        
    return res

print(productExceptSelf([1,2,3,4]))