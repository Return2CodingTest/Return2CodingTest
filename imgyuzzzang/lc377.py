# 377. Combination Sum IV

from typing import List

def combinationSum4(nums: List[int], target: int) -> int:
    dp = [0 for _ in range(target+1)]
    dp[0] = 1

    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i-num]
    
    return dp[target]
