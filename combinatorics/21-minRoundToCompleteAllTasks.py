import math

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks_dict = {}
        for task in tasks:
            if task in tasks_dict:
                tasks_dict[task]+=1
            else:
                tasks_dict[task]=1
        rounds = 0
        for task in list(tasks_dict.keys()):
            count = tasks_dict[task]
            if count==1:
                return -1
            rounds+=math.ceil(count/3)
        return rounds
    
# Leetcode Link: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/