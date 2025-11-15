class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]*len(nums)
        forward[0] = nums[0]
        backward = [1]*len(nums)
        backward[-1] = nums[-1]
        final = [1]*len(nums)
        for i in range(1,len(nums)):
            forward[i] = nums[i]*forward[i-1]
        for i in range(len(nums)-2, -1, -1):
            backward[i] = nums[i]*backward[i+1]
        final[0] = backward[1]
        final[-1] = forward[len(nums)-2]
        for i in range(1, len(final)-1):
            final[i] = forward[i-1]*backward[i+1]
        return final

# Leetcode Link : https://leetcode.com/problems/product-of-array-except-self/