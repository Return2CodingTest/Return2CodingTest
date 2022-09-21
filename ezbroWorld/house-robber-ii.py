class Solution:
    def rob(self ,nums: List[int]) -> int:
        
        if len(nums) >=1 and len(nums) <=3:
            return max(nums)
        
        numsReverse = nums[::-1]
        
        dpRight = [0] * len(nums)
        dpRight[0] = nums[0]
        dpRight[1] = max(nums[0],nums[1])
        
        dpLeft = [0] * len(nums)
        dpLeft[0] = numsReverse[0]
        dpLeft[1] = max(numsReverse[0],numsReverse[1])
                
        
        for i in range(2,len(nums)-1):
            dpRight[i] = max(dpRight[i-2]+nums[i],dpRight[i-1])
            
        for i in range(2,len(numsReverse)-1):
            dpLeft[i] = max(dpLeft[i-2]+numsReverse[i],dpLeft[i-1])
        
        return max(dpRight[len(nums)-2],dpLeft[len(numsReverse)-2])
