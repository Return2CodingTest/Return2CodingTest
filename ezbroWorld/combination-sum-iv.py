class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        global cnt
        cnt = 0
        
        def find(nums:List[int] ,target:int):
            global cnt
            
            
            for i in nums :
                if target - i < 0 :
                    continue
                    
                if target - i == 0:
                    cnt +=1
                    continue

                find(nums, target - i)


        find(nums,target)
        return cnt
