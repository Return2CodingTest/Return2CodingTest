function getSum(a: number, b: number): number {
  const and = ((a >>> 0) & (b >>> 0)) << 1;
  const xor = (a >>> 0) ^ (b >>> 0);

  return and ? getSum(xor, and) : xor;
}
