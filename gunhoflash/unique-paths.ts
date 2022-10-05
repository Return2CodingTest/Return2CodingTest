const fact = (n: number): number => n ? n * fact(n - 1) : 1;

function uniquePaths(m: number, n: number): number {
  return fact(n + m - 2) / fact(n - 1) / fact(m - 1);
}
