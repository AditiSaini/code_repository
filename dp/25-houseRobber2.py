from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size==1:
            return nums[0]
        elif size==2:
            return max(nums[0], nums[1])

        dp1 = [0]*size
        dp2 = [0]*size
        
        dp1[0] = 0
        dp2[0] = 0
        dp1[1] = nums[0]
        dp2[1] = nums[1]
        for i in range(2, size):
            dp1[i] = max(nums[i-1]+dp1[i-2], dp1[i-1])
            dp2[i] = max(nums[i]+dp2[i-2], dp2[i-1])
        return max(dp1[-1], dp2[-1])
    
# Leetcode Link: https://leetcode.com/problems/house-robber-ii/