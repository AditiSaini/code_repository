class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = nums[0] 
        count = 0 
        size = len(nums)-1
        for n in nums:
            max_reach = max(n, max_reach)
            if max_reach==0 and count!=size:
                return False
            elif max_reach > size:
                return True
            max_reach-=1
            count+=1
        return True

# Leetcode Link: https://leetcode.com/problems/jump-game/