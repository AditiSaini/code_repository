class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        char_freq = defaultdict(int)
        freq = defaultdict(int)
        for ch in s1:
            char_freq[ch]+=1
        for start in range(len(s2)):
            end = start+window
            freq = char_freq.copy()
            count = start
            found = True
            while count<end and end<=len(s2):
                cur = s2[count]
                if cur not in freq:
                    found = False
                    break
                else:
                    if freq[cur]>0:
                        freq[cur]-=1
                        if freq[cur]==0:
                            del freq[cur]
                count+=1
            if len(freq)==0 and found:
                return True
        return False

# Leetcode Link : https://leetcode.com/problems/permutation-in-string