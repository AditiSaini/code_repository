class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]* n for i in range(m) ]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                part_1 = 0
                part_2 = 0
                if i-1>=0:
                    part_1 = dp[i-1][j]
                if j-1>=0:
                    part_2 = dp[i][j-1]
                dp[i][j] = part_1 + part_2
        return dp[m-1][n-1]
    
# Leetcode Link: https://leetcode.com/problems/unique-paths