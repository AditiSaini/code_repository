from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        all_intervals = [intervals_sorted[0]]
        for idx in range(1, len(intervals_sorted)):
            prev_interval = all_intervals[-1]
            interval = intervals_sorted[idx]
            if prev_interval[1]>=interval[0]:
                all_intervals.pop()
                all_intervals.append([prev_interval[0], max(interval[1], prev_interval[1])])
            else:
                all_intervals.append(interval)
        return all_intervals

# Leetcode Link: https://leetcode.com/problems/merge-intervals/