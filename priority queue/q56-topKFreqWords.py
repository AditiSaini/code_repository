import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        out = []
        freq = defaultdict(lambda: 0)
        for w in words:
            freq[w]+=1
        list_freq = [(-1*value, key) for key, value in freq.items()]
        heapq.heapify(list_freq)   
        for i in range(k):
            _, key = heapq.heappop(list_freq)
            out.append(key)
        return out

# Leetcode Link: https://leetcode.com/problems/top-k-frequent-words/