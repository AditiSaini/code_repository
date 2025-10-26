class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        length = len(s)
        if length==0:
            return 0
        max_length = 1
        char_set_observed = set()
        char_set_observed.add(s[left])
        for right in range(1, length):
            char = s[right]
            while char in char_set_observed and left<=right:
                char_set_observed.remove(s[left])
                left+=1
            char_set_observed.add(char)
            max_length = max(max_length, right - left + 1)
        return max_length 

# Leetcode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/