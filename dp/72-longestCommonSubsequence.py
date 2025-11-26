class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_t1 = len(text1)
        len_t2 = len(text2)
        dp = [[0]*(len_t1+1) for _ in range(len_t2+1)]
        text1 = '0'+text1
        text2 = '0'+text2
        for t2 in range(1, len_t2+1):
            for t1 in range(1, len_t1+1):
                if text1[t1]==text2[t2]:
                    dp[t2][t1] = dp[t2-1][t1-1]+1
                else:
                    dp[t2][t1] = max(dp[t2-1][t1], dp[t2][t1-1])
        return dp[-1][-1]
    
# Leetcode Link : https://leetcode.com/problems/longest-common-subsequence/