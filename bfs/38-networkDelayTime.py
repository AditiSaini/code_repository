from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((end, weight))
        shortest_time = {}
        min_queue = []
        heapq.heappush(min_queue, (0, k))
        while len(min_queue)>0:
            time, node = heapq.heappop(min_queue)
            if node in shortest_time:
                continue
            shortest_time[node] = time 
            if len(shortest_time)==n:
                break
            if len(graph[node])>0:
                for neighbor, weight in graph[node]:
                    heapq.heappush(min_queue, (time+weight, neighbor))
        if len(shortest_time)!=n:
            return -1
        return max(shortest_time.values())

# Leetcode Link: https://leetcode.com/problems/network-delay-time/