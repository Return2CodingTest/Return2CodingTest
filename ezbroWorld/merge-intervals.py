class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #상수 설정
        START, END = 0, 1
        #시작점 기준 정렬
        intervals.sort(key = lambda x:x[0])
        #길이 설정
        length = len(intervals)

        #merge하게 될 Interval 인덱스 처음과 끝
        mergeIntervalStart = -1
        mergeIntervalEnd = -1

        result =[]

        for i in range(length) : 
            if i <= mergeIntervalEnd : continue

            mergeIntervalStart = i
            mergeIntervalEnd = i
            startPos = intervals[i][START]
            endPos = intervals[i][END]

            for j in range(i+1, length) :
                if endPos >= intervals[j][START] :
                    mergeIntervalEnd = j
                    endPos = max(endPos, intervals[j][END])
                elif endPos < intervals[j][START] :
                    break

            result += [[startPos,endPos]]
            
        return result
