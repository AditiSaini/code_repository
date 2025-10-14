from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_ptr = maxFreq = 0 
        maxLen = 1
        counter = defaultdict(int)
        counter[s[left_ptr]] = 1
        for right_ptr in range(1, len(s)):
            counter[s[right_ptr]]+=1
            maxFreq = max(maxFreq, counter[s[right_ptr]])
            window = right_ptr - left_ptr + 1
            if window - maxFreq > k:
                counter[s[left_ptr]]-=1
                left_ptr+=1
                maxFreq-=1
            else:
                maxLen = max(maxLen, window)
        return maxLen

# Leetcode Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/