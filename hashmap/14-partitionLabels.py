from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Step 1: convert to dictionary with index range
        chars = {}
        for idx in range(len(s)):
            char = s[idx]
            if char in chars:
                chars[char] = [chars[char][0], idx]
            else:
                chars[char] = [idx, idx]
        #Step 2: merge intervals when overlapping
        intervals = []
        char_keys = list(chars.keys())
        prev_interval = chars[char_keys[0]]
        for char in char_keys[1:]:
            current_interval = chars[char]
            start = current_interval[0]
            end = current_interval[1]
            prev_start = prev_interval[0]
            prev_end = prev_interval[1]
            #Don't overlap
            if start>prev_end:
                intervals.append([prev_start, prev_end])
                prev_interval = [start, end]
            #They overlap 
            else:
                prev_interval = [min(start, prev_start), max(end, prev_end)]
        intervals.append(prev_interval)
        #Step 3: compute numbers for partition
        final = []
        for interval in intervals:
            final.append(interval[1]-interval[0]+1)
        return final

s = Solution()
testcases = ["ababcbacadefegdehijhklij"]
print(s.partitionLabels(testcases[0]))