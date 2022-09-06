#198. House Robber

from typing import List

def rob(nums: List[int]) -> int:
        dp = nums[:]
        
        if len(dp) > 2:
            dp[2] += dp[0]
            
            for i in range(3, len(dp)):
                dp[i] += max(dp[i-2], dp[i-3]) 

        return max(dp)
            