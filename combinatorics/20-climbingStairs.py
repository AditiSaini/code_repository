class Solution:
    def climbStairs(self, n: int) -> int:
        steps = 0
        steps_prev_1 = 0
        steps_prev_2 = 0
        for i in range(1, n+1):
            steps_prev_2 = steps_prev_1
            steps_prev_1 = steps
            if i==1:
                steps = 1
            elif i==2:
                steps = 2
            else:
                steps = steps_prev_1 + steps_prev_2
        return steps

# Leetcode Link: https://leetcode.com/problems/climbing-stairs/