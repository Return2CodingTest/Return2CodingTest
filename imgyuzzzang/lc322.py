# 322. Coin Change

from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    dp = {}
    isBreakPoint = False

    for coin in coins:
        if coin < amount:
            dp[coin] = 1
        if(coin == amount):
            return 1

    for amount_a in dp:
        for amount_b in dp:
            if amount_a + amount_b > amount:
                continue
            if amount_a + amount_b in dp:
                dp[amount_a + amount_b] = min(dp[amount_a]+dp[amount_b] , dp[amount_a + amount_b])
            else:
                dp[amount_a + amount_b] = dp[amount_a]+dp[amount_b]
        
        coinCount += 1
    
#unsolved