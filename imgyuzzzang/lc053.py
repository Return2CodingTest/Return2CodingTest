# 53. Maximum Subarray
from typing import List

def maxSubArray(nums: List[int]) -> int:
    n = len(nums)
    for i in range(1,n):
        nums[i] = max(nums[i], nums[i] + nums[i-1])
        
    return max(nums)


#print(maxSubArray([5,4,-1,7,8]))  
#print(maxSubArray([1]))  
print(maxSubArray([-3,1,0,-1,-2,3,2,-1]))  
