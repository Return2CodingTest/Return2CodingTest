function rob(nums: number[]): number {
  let answerPrevPrev = 0;
  let answerPrev = 0;
  let answerNow = 0;

  for (const num of nums) {
    answerNow = Math.max(answerPrevPrev + num, answerPrev);
    answerPrevPrev = answerPrev;
    answerPrev = answerNow;
  }

  return Math.max(answerNow, answerPrev);
}
