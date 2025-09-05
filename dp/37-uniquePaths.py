#My solution 1 using recursion with memoization

from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def findPaths(j, k):
            if j==(m-1) and k==(n-1):
                return 1
            right = down = 0
            if (k+1)<n:
                right = findPaths(j, k+1)
            if (j+1)<m:
                down = findPaths(j+1, k)
            return right + down 
        return findPaths(0, 0)

#Chat GPT solution 2 using dp

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n]*m
        for j in range(1, m):
            for k in range(1, n):
                dp[j][k] = dp[j-1][k]+dp[j][k-1]
        return dp[m-1][n-1]
