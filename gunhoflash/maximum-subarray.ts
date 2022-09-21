function maxSubArray(nums: number[]): number {
  let sumFromStart = 0;
  let minSum = 0;
  let maxSum = nums[0];

  for (const num of nums) {
    sumFromStart += num;
    maxSum = Math.max(maxSum, sumFromStart - minSum);
    minSum = Math.min(minSum, sumFromStart);
  }

  return maxSum;
}
