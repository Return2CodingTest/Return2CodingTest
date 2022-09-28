# 213. House Robber II

from typing import List

def rob(nums: List[int]) -> int:
        dpIncludeFirst = nums[:]
        dpExcludeFirst = nums[:]
        n = len(nums)

        if n > 3:
            dpIncludeFirst[2] += dpIncludeFirst[0]
            dpExcludeFirst[3] += dpExcludeFirst[1]
            for i in range(3, n-1):
                dpIncludeFirst[i] += max(dpIncludeFirst[i-2], dpIncludeFirst[i-3])
                dpExcludeFirst[i+1] += max(dpExcludeFirst[i-1], dpExcludeFirst[i-2])
        
        return max(dpIncludeFirst + dpExcludeFirst)