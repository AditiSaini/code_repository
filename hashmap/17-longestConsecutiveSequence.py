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
    
# Leetcode Link: https://leetcode.com/problems/longest-consecutive-sequence