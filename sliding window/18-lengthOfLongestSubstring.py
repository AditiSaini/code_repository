class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        start = 0
        end = 1
        data_set = set(s[start])
        max_count = 1
        cur_char_start = s[start]
        cur_char_end = s[end]
        while end<len(s):
            cur_char_end = s[end]
            while cur_char_end in data_set:
                data_set.remove(cur_char_start)
                start+=1
                cur_char_start = s[start]
            data_set.add(cur_char_end)
            max_count = max(max_count, len(data_set))
            end+=1
        return max_count
    
# Leetcode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters