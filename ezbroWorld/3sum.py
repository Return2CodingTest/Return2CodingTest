class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # two point
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                # sum < 0 이면 left를 땡겨줌
                if sum < 0:
                    left +=1
                # sum > 0 이면 right를 땡겨줌    
                elif sum > 0 :
                    right -= 1
                
                # sum = 0 이면,,,
                else : 
                    result.append([nums[i],nums[left],nums[right]])
                    
                    while left<right and nums[left] == nums[left +1]:
                        left +=1
                    while left<right and nums[right] == nums[right -1]:
                        right -=1
                    
                    left +=1
                    right -=1
        
        return result
