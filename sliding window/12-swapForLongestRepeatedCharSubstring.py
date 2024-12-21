class Solution:
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
testcases = ["ababa", "aaabaaa", "aaaaa", "bbababaaaa"]
print(s.maxRepOpt1(testcases[3]))