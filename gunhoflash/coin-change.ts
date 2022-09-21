const NULL = -1;

function coinChange(coins: number[], amount: number): number {
  const fewestNumberOfCoins = Array(amount + 1).fill(NULL);

  fewestNumberOfCoins[0] = 0;

  for (let i = 0; i <= amount; i++) {
    const candidates = coins
      .filter(v => v <= i)
      .map(v => fewestNumberOfCoins[i - v])
      .filter(v => v !== NULL);

    if (candidates.length) {
      fewestNumberOfCoins[i] = Math.min(...candidates) + 1;
    }
  }

  return fewestNumberOfCoins[amount];
}
