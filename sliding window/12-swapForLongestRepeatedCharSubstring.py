class Solution:
    def maxRepOpt2(self, text: str) -> int:
        res = 0
        groups = {}
        for idx in range(len(text)):
            ch = text[idx]
            if ch in groups:
                groups[ch].append(idx)
            else:
                groups[ch] = [idx]
        for ch in groups:
            cur = 1
            pre = 0
            SUM = 0
            for idx in range(1, len(groups[ch])):
                prev_index = groups[ch][idx-1]
                index = groups[ch][idx]
                #Index difference 1
                if index == prev_index+1:
                    cur+=1
                #Index difference 2 (skip one char)
                elif index == prev_index+2:
                    pre = cur
                    cur = 1
                #More than one char difference
                else:
                    cur = 1
                    pre = 0
                SUM = max(SUM, cur+pre)
            if SUM < len(groups[ch]):
                SUM+=1
            res = max(res, SUM)
        return res
    
    def maxRepOpt1(self, text: str) -> int:
        text_dict = {}
        max_len_possible = 1
        for char in text:
            text_dict[char] = text_dict.get(char, 0)+1
            if text_dict[char]>max_len_possible:
                max_len_possible = text_dict[char]
        max_repeated_char = 1
        current_repeated_char = 1
        max_skip = min(1, len(text)-max_len_possible)
        for idx in range(len(text)):
            char = text[idx]
            count = idx+1
            prev_char = text[idx]
            current_repeated_char = 1
            max_skip = min(1, len(text)-max_len_possible)
            while count<len(text):
                current_char = text[count]
                if current_char==prev_char and current_repeated_char<text_dict[prev_char]:
                    current_repeated_char+=1
                    max_repeated_char = max(max_repeated_char, current_repeated_char)
                elif max_skip>0 and current_repeated_char<text_dict[prev_char]:
                    current_repeated_char+=1
                    max_skip-=1
                    max_repeated_char = max(max_repeated_char, current_repeated_char)
                else:
                    break
                count+=1
        return max_repeated_char

s = Solution()
testcases = ["aaabbaaa", "acbaaa", "ababa", "aaabaaa", "aaaaa", "bbababaaaa"]
print(s.maxRepOpt2(testcases[2]))