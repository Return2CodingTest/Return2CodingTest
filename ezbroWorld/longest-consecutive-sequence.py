class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxNum= 0
        setNums = set(nums)
        
        cnt =0
        
        for num in nums :   
            if (num-1) not in nums :
                    
                currentNum = num
                currentMaxNum = 1
                
                while currentNum+1 in setNums:
                    currentNum += 1
                    currentMaxNum +=1
                    
                maxNum= max(maxNum, currentMaxNum)
                
        return maxNum
