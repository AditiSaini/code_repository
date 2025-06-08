class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height)-1
        max_water_amt = 0
        cur_water_amt = 0
        while left_ptr<right_ptr:
            #1. Calculate and update water amount if needed
            cur_water_amt = min(height[left_ptr], height[right_ptr])*(right_ptr - left_ptr)
            if cur_water_amt>max_water_amt:
                max_water_amt = cur_water_amt 
            #2. Decrement the left/right based on which has a lower height value
            if height[left_ptr]>height[right_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1
        return max_water_amt 