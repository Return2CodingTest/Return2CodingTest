function updateMinWithLowerbound(num: number, nums: number[]) {
  let left = 0, right = nums.length;

  while (left < right) {
    const midIndex = (left + right) >> 1;
    const midValue = nums[midIndex];

    if (midValue >= num) {
      right = midIndex;
    } else {
      left = midIndex + 1;
    }
  }

  nums[left] = num;
}

function lengthOfLIS(nums: number[]): number {
  const lis = [Infinity];
  nums.forEach(num => updateMinWithLowerbound(num, lis));
  return lis.length;
}
