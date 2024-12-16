import heapq
import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ordered_k_points = []
        heap = []
        count = 0
        for idx in range(len(points)):
            point = points[idx]
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(heap, (distance, point))
        while count<k:
            distance, to_add_point = heapq.heappop(heap)
            ordered_k_points.append(to_add_point)
            count+=1
        return ordered_k_points

#Meta 