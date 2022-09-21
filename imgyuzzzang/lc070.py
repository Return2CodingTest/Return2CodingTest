# 70. Climbing Stairs

def climbStairs(n: int) -> int:
    dp = [1,2]
    for i in range(2,n):
        dp.append(dp[i-2] + dp[i-1])
    
    return dp[n-1]

print(climbStairs(4))