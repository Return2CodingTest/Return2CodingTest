from typing import List

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    NULL = -1
    fewestNumberOfCoins = [NULL] * (amount + 1)
    fewestNumberOfCoins[0] = 0

    for i in range(amount + 1):
      candidates = list(
        filter(
          lambda v: v != NULL,
          map(
            lambda v: fewestNumberOfCoins[i - v],
            filter(
              lambda v: v <= i,
              coins
            )
          )
        )
      )

      if len(candidates):
        fewestNumberOfCoins[i] = min(candidates) + 1

    return fewestNumberOfCoins[amount]
