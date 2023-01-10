function topKFrequent(nums: number[], k: number): number[] {
  const counter = new Map<number, number>();
  nums.forEach(n => counter.set(n, (counter.get(n) ?? 0) + 1));
  return Array.from(counter.entries())
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map(v => v[0]);
}
