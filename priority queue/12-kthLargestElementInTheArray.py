import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        count = 0
        while count<k:
            popped = heapq.heappop(heap)
            count+=1
        return -popped