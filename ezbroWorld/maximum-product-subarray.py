class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin,result = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            x = max(curMax*nums[i],curMin*nums[i],nums[i])
            y = min(curMax*nums[i],curMin*nums[i],nums[i])
            curMax = x
            curMin = y
            result = max(curMax,result)
        return result
