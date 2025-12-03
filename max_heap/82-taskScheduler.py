from collections import defaultdict, deque
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for t in tasks:
            freq[t]+=1
        queue = deque()
        max_heap = [ (-val, key) for key, val in freq.items()]
        heapq.heapify(max_heap)
        scheduled = []
        time = 0 
        while max_heap or queue:
            time+=1
            if max_heap:
                val, key = heapq.heappop(max_heap)
                scheduled.append(key)
                if val+1!=0:
                    queue.append((time+n, key, val+1))
            else:
                scheduled.append('idle')
            if queue and queue[0][0]==time:
                _, key, val = queue.popleft()
                heapq.heappush(max_heap, (val, key))
        return time

# Leetcode Link : https://leetcode.com/problems/task-scheduler/