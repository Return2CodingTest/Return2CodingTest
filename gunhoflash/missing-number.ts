function missingNumber(nums: number[]): number {
  const max = nums.length;
  return (max * (max + 1) / 2) - nums.reduce((sum, num) => sum + num, 0);
}
