class Solution:
    def canJump(self, nums: List[int]) -> bool:
        total_gas = nums[0] 
        count = 0 
        for n in nums:
            if n>total_gas:
                total_gas = n
            if total_gas==0 and count!=(len(nums)-1):
                return False
            total_gas-=1
            count+=1
        return True

# Leetcode Link: https://leetcode.com/problems/jump-game/