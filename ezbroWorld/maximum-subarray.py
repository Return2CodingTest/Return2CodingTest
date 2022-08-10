class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArr = [0]*len(nums)
        maxArr[0] = nums[0]
        for i in range(1,len(nums)):
            maxArr[i] = max(maxArr[i-1] + nums[i], nums[i])
        return max(maxArr)
