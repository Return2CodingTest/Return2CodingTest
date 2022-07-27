class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # when n = [1,2,3,4],
        # output = [n[1]*n[2]*n[3], n[0] * n[2]*n[3], n[0]*n[1] * n[3], n[0]*n[1]*n[2]]
        result = [1 for i in range(len(nums))]
        leftToRight = [1 for i in range(len(nums))]
        rightToLeft = [1 for i in range(len(nums))]
        tmp1,tmp2 = nums[0], nums[len(nums)-1]
        
        # 1, 2, 3
        for i in range(1,len(nums)):
            leftToRight[i] *= tmp1
            tmp1 *= nums[i]
            
        # 2, 1, 0
        for i in range(len(nums)-2,-1,-1):
            rightToLeft[i] *= tmp2
            tmp2 *= nums[i]
            
        for i in range(len(nums)):
            result[i] = leftToRight[i]*rightToLeft[i]
            
        return result
