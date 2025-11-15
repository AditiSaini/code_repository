class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums)<=1:
            return n
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

# Leetcode Link : https://leetcode.com/problems/longest-increasing-subsequence/