function findMin(nums: number[]): number {
  let leftIndex = 0;
  let rightIndex = nums.length - 1;

  while (leftIndex < rightIndex) {
    const midIndex = Math.floor((leftIndex + rightIndex) / 2);
    const midValue = nums[midIndex];
    const rightValue = nums[rightIndex];
  
    if (midValue < rightValue) {
      rightIndex = midIndex;
    } else {
      leftIndex = midIndex + 1;
    }
  }

  return nums[leftIndex];
}
