class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervalsLength= len(intervals)
        result=[-1,10001]
        resultIntervals=[[]]
        
        for i in range(0,intervalsLength,1) :
            if newInterval[0] < intervals[i][0] :
                if intervals[i-1][1] < newInterval[0] :
                    result[0] = newInterval[0]
                else : 
                    result[0] = intervals[i][0]
                    
        for j in range(intervalsLength-1,-1,-1) :
            if intervals[j][1] > newInterval[1] :
                if intervals[j+1][0] > newInterval[1] :
                    result[1] = newInterval[1]
                else : 
                    result[1] = intervals[j][1]
        
        
        for k in range(0,intervalsLength) : 
            if result[0] <= intervals[k][0]:
                resultIntervals + intervals[0:k]
                break
                
        resultIntervals.append(result)
        
        for l in range(0, intervalsLength) : 
            if result[1] <= intervals[l][1] :
                resultIntervals + intervals[l+1:intervalsLength]
                
        return resultIntervals
