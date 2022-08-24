# 300. Longest Increasing Subsequence

from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    dp = dict.fromkeys(nums,0)

    def saveDp(i, n):
        if i in dp:
            dp[i] = max(dp[i], n)
        else:
            dp[i] = n
    
    for num in nums:
        for i in dp: 
            if i < num:
                saveDp(num, dp[i] + 1)
        saveDp(num, 1)
    print(dp)
    return max(dp.values())
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([3,2,1]))