function canJump(nums: number[]): boolean {
  // obviously, the last index is reachable to itself
  let closestReachableIndex = nums.length - 1;
  
  // search reachable indexes from last index to start index
  for (let i = nums.length - 2; i >= 0 ; i--) {
    if (i + nums[i] >= closestReachableIndex) {
      closestReachableIndex = i;
    }
  }
  
  return closestReachableIndex === 0;
}
