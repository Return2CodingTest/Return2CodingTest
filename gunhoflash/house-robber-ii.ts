function robLinear(nums: number[]): number {
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

function rob(nums: number[]): number {
  // 첫 집을 턴다면: 마지막 집은 못 터므로 이를 제거하고 선형으로 풀이한다.
  // 첫 집을 안 턴다면: 첫 집을 제거하고 선형으로 풀이한다.
  // 예외: 집이 하나 뿐이라면 위 방법을 사용하지 말아야 한다.
  if (nums.length <= 2) {
    return Math.max(...nums);
  }

  return Math.max(
    robLinear(nums.slice(1)),
    robLinear(nums.slice(0, nums.length - 1))
  );
}
