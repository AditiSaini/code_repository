class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size==1:
            return nums[0]
        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]
    
# Leetcode Link: https://leetcode.com/problems/house-robber/