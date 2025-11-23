class Solution:
    def findMaxInDict(self, freq):
        max_freq = 0
        max_char = ""
        for ch in freq:
            if freq[ch]>max_freq:
                max_char = ch
                max_freq = freq[ch]
        return max_freq, max_char
    def maxRepOpt1(self, text: str) -> int:
        left = 0
        window_freq = defaultdict(int)
        window_size = 0
        max_freq = 0
        longest_size = 0
        all_freq = defaultdict(int)
        for ch in text:
            all_freq[ch]+=1
        for right, ch in enumerate(text):
            window_freq[ch]+=1
            max_freq, max_char = self.findMaxInDict(window_freq)
            window_size = right-left+1
            while (window_size - max_freq > 1 or window_size > all_freq[max_char]) and left + 1 < len(text):
                window_freq[text[left]]-=1
                left+=1
                window_size-=1
                max_freq, max_char = self.findMaxInDict(window_freq)
            longest_size = max(longest_size, window_size)
        return longest_size
            
# Leetcode Link : https://leetcode.com/problems/swap-for-longest-repeated-character-substring/