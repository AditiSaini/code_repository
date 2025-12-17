class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_left = 0
        max_right = 0
        water = 0 
        cur_val = "left"
        while left<right:
            left_height = height[left]
            right_height = height[right]
            max_left = max(max_left, left_height)
            max_right = max(max_right, right_height)
            if cur_val=="left":
                water+=(max_left-left_height)
            else:
                water+=(max_right-right_height)
            if max_left < max_right:
                left+=1
                cur_val = "left"
            else:
                right-=1
                cur_val = "right"
        return water

# Leetcode Link : https://leetcode.com/problems/trapping-rain-water/