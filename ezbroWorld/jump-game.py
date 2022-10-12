class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        lastIndex = len(nums)-1
        canGo = [0]*len(nums)
        for i in range(len(nums)):
            canGo[i] += (i + nums[i])
        
        # 2 1 0 1 4 -> nums
        # 2 2 4 4 8 -> canGo
        # 0 1 2 3 4 -> index
        # check if canGo == lastIndex
        # if true, nowIndex로 갈 놈 이 있는지 찾음
        #   check if canGo == nowIndex
        # shouldFindValue
        shouldFindValue = len(nums)-1
        for i in range(len(nums)-1,-1,-1) :
            if canGo[i] >= shouldFindValue :
                shouldFindValue = i
            
        # 3 2 1 0 4
        # 0 1 2 3 4
        # 3 3 3 3 4
        
        # 2 3 1 1 4
        # 0 1 2 3 4
        # 2 4 3 4 8
        
        if shouldFindValue == 0 : 
            return True
        
        return False
