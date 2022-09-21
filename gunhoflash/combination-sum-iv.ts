function combinationSum4(nums: number[], target: number): number {
  const answers = Array(target + 1).fill(0);
  answers[0] = 1;

  for (let i = 1; i <= target; i++) {
    for (const num of nums) {
      if (num <= i) {
        answers[i] += answers[i - num];
      }
    }
  }

  return answers[target];
}
