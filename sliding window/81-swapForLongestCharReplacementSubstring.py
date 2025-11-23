class Solution:
    def getMaxFreqDict(self, freq):
        maxChar = ""
        maxFreq = 0
        for ch in freq:
            if freq[ch]>maxFreq:
                maxFreq = freq[ch]
                maxChar = ch
        return maxFreq, maxChar

    def maxRepOpt1(self, text: str) -> int:
        max_freq = 0
        all_freq = defaultdict(int)
        for ch in text:
            all_freq[ch]+=1
        left = 0 
        window = 0
        freq_window = defaultdict(int)
        longest = 0
        for right, ch in enumerate(text):
            freq_window[ch]+=1
            max_freq, max_char = self.getMaxFreqDict(freq_window)
            window = right-left+1
            while window-max_freq>1:
                freq_window[text[left]]-=1
                left+=1
                window-=1
            longest = max(longest, min(window, all_freq[max_char]))
        return longest 
            
# Leetcode Link : https://leetcode.com/problems/swap-for-longest-repeated-character-substring/