class Solution:
    def climbStairs(self, n: int) -> int:
        buffer = {}
        def climb_recurse(current_step, n):
            if current_step == n:
                buffer[current_step] = 1
                return 1
            elif current_step > n:
                buffer[current_step] = 0
                return 0
            else:
                if current_step+1 not in buffer.keys():
                    data1 = climb_recurse(current_step+1, n) 
                    buffer[current_step+1] = data1
                else:
                    data1 = buffer[current_step+1]
                if current_step+2 not in buffer.keys():
                    data2 = climb_recurse(current_step+2, n) 
                    buffer[current_step+2] = data2
                else:
                    data2 = buffer[current_step+2]
                return data1 + data2
        return climb_recurse(0, n)