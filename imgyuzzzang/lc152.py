# 152. Maximum Product Subarray
from typing import List

def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    minus = nums[:]
    plus = nums[:]

    for i in range(1, n):
        minus[i] = min(nums[i], nums[i] * plus[i-1], nums[i] * minus[i-1])
        plus[i] = max(nums[i], nums[i] * plus[i-1], nums[i] * minus[i-1])
    
    return max(plus)