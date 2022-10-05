from functools import cmp_to_key
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        def myCompare(a,b):
            if a[1] > b[1] : #열 오름차순
               return 1
            elif a[1] == b[1] : 
                if a[0] < b[0] : #행 내림차순
                   return 1
                elif a[0] == b[0] :
                   return 0
                else :
                   return -1
                return 0
            else : 
                return -1    
                
        intervals.sort(key = cmp_to_key(myCompare))
        count = 0
        last = -999999999
        for start,end in intervals : 
            if start < last : count+=1 # 겹침
            else : last = end

        return count

  
