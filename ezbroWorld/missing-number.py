class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tmpArr=nums[:]
        tmpArr.sort()
        for i in range(len(tmpArr)):
            if tmpArr[i] != i : return i
            
        return len(tmpArr)
