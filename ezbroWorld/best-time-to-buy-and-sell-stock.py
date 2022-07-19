class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for pointer in range(1, len(prices)):
            if min > prices[pointer] : 
                min = prices[pointer]
            elif min <= prices[pointer] : 
                profit = max(profit,prices[pointer]-min)
                
        return profit
