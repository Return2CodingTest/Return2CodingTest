# 121. Best Time to Buy and Sell Stock
from typing import List

def maxProfit(prices: List[int]) -> int:
    min = prices[0]
    max_diff = 0
    
    for i in prices:
        if min > i:
            min = i
        if max_diff < i - min:
            max_diff = i - min
    
    return max_diff

print(maxProfit([7,1,5,3,6,4]))