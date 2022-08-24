# 268. Missing Number
from collections import Counter
from typing import List

def missingNumber(nums: List[int]) -> int:
    numberCount = Counter(nums)
    n = len(nums)

    for i in range(n+1):
        if not i in numberCount:
            return i

print(missingNumber([3,0,1]))
