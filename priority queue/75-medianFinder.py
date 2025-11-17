import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.len = 0 

    def addNum(self, num: int) -> None:
        self.len+=1
        if not self.max_heap or num<=-1*self.max_heap[0]:
            heapq.heappush(self.max_heap, -1*num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap)>len(self.min_heap)+1:
            heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))
        elif len(self.min_heap)>len(self.max_heap):
            heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if self.len%2==1:
            return -1*self.max_heap[0]
        return (-1*self.max_heap[0]+ self.min_heap[0])/2
    
# Leetcode Link : https://leetcode.com/problems/find-median-from-data-stream