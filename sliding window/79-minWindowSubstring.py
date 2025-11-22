## ATTEMPT 1: Needs Improvement

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = defaultdict(int)
        for i in range(len(t)):
            cur = t[i]
            freq_t[cur]+=1
        min_window = float('inf')
        window = ""
        for count in range(len(s)):
            cur = s[count]
            i = count
            new_freq_t = freq_t.copy()
            while i<len(s) and len(new_freq_t)>0:
                now = s[i]
                if now in new_freq_t:
                    new_freq_t[now]-=1
                    if new_freq_t[now]==0:
                        del new_freq_t[now]
                i+=1
            if len(new_freq_t)==0:
                min_window = min(min_window, i-count)
                if (i-count)==min_window:
                    window = s[count:i]
        return window

## ATTEMPT 2: Better Solution

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        window = (0, float('inf'))
        start_index = 0
        target_remaining = len(t)
        freq_t = defaultdict(int)
        for char in t:
            freq_t[char]+=1
        for end_index, ch in enumerate(s):
            if freq_t[ch]>0:
                target_remaining -= 1
            freq_t[ch]-=1
            if target_remaining == 0:
                while True:
                    cur = s[start_index]
                    if freq_t[cur] == 0:
                        break
                    start_index+=1
                    freq_t[cur]+=1
                if (window[1]-window[0])>(end_index - start_index):
                    window = (start_index, end_index)
                freq_t[s[start_index]]+=1
                start_index+=1
                target_remaining+=1
        if window[1]<len(s):
            return s[window[0]: window[1]+1]
        return ""

# Leetcode Link : https://leetcode.com/problems/minimum-window-substring/