function maxProfit(prices: number[]): number {
  let profit = 0;
  let minPrice = 10000;

  for (const price of prices) {
    minPrice = Math.min(minPrice, price);
    profit = Math.max(profit, price - minPrice);
  }

  return profit;
}
