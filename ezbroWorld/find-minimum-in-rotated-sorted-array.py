class Solution:
    def findMin(self, nums: List[int]) -> int:
        a=nums[:]
        first, end= 0, len(a)-1
        result = -1
        while True:
            if a[first] <= a[end]:
                result = a[first]
                break
                
            if (end-first) == 1 : 
                result = min(a[end],a[first])
                break
            
            if a[first] > a[end]:
                mid = (first + end) // 2
                
                if a[first] > a[mid]:
                    end = mid
                    continue
        
                if a[end] < a[mid]:
                    first = mid
                    continue
                    
        return result
