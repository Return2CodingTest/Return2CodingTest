function hammingWeight(n: number): number {
  let answer = 0;
  while (n) {
    answer += n & 1;
    n >>>= 1;
  }

  return answer;
}
