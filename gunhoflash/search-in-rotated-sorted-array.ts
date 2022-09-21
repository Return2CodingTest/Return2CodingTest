function search(nums: number[], target: number): number {
  let leftIndex = 0;
  let rightIndex = nums.length - 1;

  while (leftIndex < rightIndex) {
    const midIndex = Math.floor((leftIndex + rightIndex) / 2);
    const leftValue = nums[leftIndex];
    const midValue = nums[midIndex];
    const rightValue = nums[rightIndex];

    if (midValue === target) return midIndex;

    if (leftValue <= midValue) {
      if (leftValue <= target && target <= midValue) {
        rightIndex = midIndex;
      } else {
        leftIndex = midIndex + 1;
      }
    } else if (midValue <= target && target <= rightValue) {
      leftIndex = midIndex + 1;
    } else {
      rightIndex = midIndex;
    }
  }

  return nums[leftIndex] === target ? leftIndex : -1;
}
