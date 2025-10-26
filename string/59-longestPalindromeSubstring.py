class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s)==1:
            return s

        def expand(l, r, s):
            result = ""
            while l<=r and l>=0 and r<len(s):
                cur_left = s[l]
                cur_right = s[r]
                if cur_left == cur_right:
                    if len(result)<len(s[l:r+1]):
                        result = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
            return result
        
        result = ""
        for center in range(len(s)-1):
            result1 = expand(center, center, s)
            result2 = expand(center, center+1, s)
            len_result1 = len(result1)
            len_result2 = len(result2)
            if len(result)<max(len_result1, len_result2):
                if len_result1>len_result2:
                    result = result1
                else:
                    result = result2
        return result 

# Leetcode Link: https://leetcode.com/problems/longest-palindromic-substring/