import heapq

class MedianFinder:
    pq = []

    def __init__(self):
        self.pq = []
        
    def getNthInPq(self, n, count = 1):
        print(self.pq, n, count)
        print(heapq.nsmallest(n+1, self.pq))
        return list(heapq.nsmallest(n+1, self.pq))[n:n+count]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.pq, num)

    def findMedian(self) -> float:
        n = len(self.pq)
        print(n)
        if n & 1:
            midIndex = int((n-1)/2)
            return self.getNthInPq(midIndex)
        else:
            midIndex = int(n/2)
            return sum(self.getNthInPq(midIndex-1, 2))/2