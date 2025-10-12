class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        min_prod = max_prod = result = nums[0] 
        for n in nums[1:]:
            if n<0:
                max_prod, min_prod = min_prod, max_prod 
            min_prod = min(n, min_prod*n)
            max_prod = max(n, max_prod*n)
            result = max(result, max_prod)
        return result
    
# Leetcode Link: https://leetcode.com/problems/maximum-product-subarray/