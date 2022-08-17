function climbStairs(n: number): number {
  let prevPrevStep = 0;
  let prevStep = 1;
  let step = 0;

  while (n--) {
    step = prevPrevStep + prevStep;
    prevPrevStep = prevStep;
    prevStep = step;
  }

  return step;
}
