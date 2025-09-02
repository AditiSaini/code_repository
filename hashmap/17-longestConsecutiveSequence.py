from typing import List

#Attempt 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==0:
            return 0
        nums_dict = set(nums)
        max_count = 1
        for cur_num in nums_dict:
            if ((cur_num - 1) not in nums_dict):
                count = 1
                while (cur_num + 1 in nums_dict):
                    count+=1
                    cur_num+=1
                max_count = max(count, max_count)
        return max_count 

#Attempt 2
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==0:
            return 1
        observed = set()
        max_seq_len = 1
        observed = set(nums)
        for n in observed:
            if (n-1) not in observed:
                count = 1
                while (n+count) in observed:
                    count+=1
                max_seq_len = max(max_seq_len, count)
        return max_seq_len
    
# Leetcode Link: https://leetcode.com/problems/longest-consecutive-sequence