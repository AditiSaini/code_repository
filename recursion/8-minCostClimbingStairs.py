class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        buffer = {}
        def recurseClimbingStairs(current_pos, cost, top):
            if current_pos==top:
                buffer[current_pos] = 0
                return 0
            elif current_pos > top:
                buffer[current_pos] = float('inf')
                return float('inf')
            else:
                if current_pos+1 in buffer.keys():
                    cost1 = cost[current_pos] + buffer[current_pos+1]
                else:
                    temp = recurseClimbingStairs(current_pos+1, cost, top)
                    buffer[current_pos+1] = temp
                    cost1 = cost[current_pos] + temp
                if current_pos+2 in buffer.keys():
                    cost2 = cost[current_pos] + buffer[current_pos+2]
                else:
                    temp = recurseClimbingStairs(current_pos+2, cost, top)
                    buffer[current_pos+2] = temp
                    cost2 = cost[current_pos] + temp
                return min(cost1, cost2)
        top = len(cost)
        start1_cost = recurseClimbingStairs(0, cost, top)
        start2_cost = recurseClimbingStairs(1, cost, top)
        return min(start1_cost, start2_cost)
        