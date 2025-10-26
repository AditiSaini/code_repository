class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)-1
        start = 0 
        end = length
        cur = start + 1
        while cur<=end and nums[cur]>=nums[start]:
            start = cur
            cur+=1
        cur = end - 1
        while cur>=0 and nums[cur]<=nums[end]:
            end = cur
            cur-=1
        if start==length and end==0:
            return 0 
        min_ = min(nums[start: end+1])
        max_ = max(nums[start: end+1])
        cur = start - 1
        while cur>=0 and nums[cur]>min_:
            start = cur
            cur-=1
        cur = end + 1
        while cur<=length and nums[cur]<max_:
            end = cur 
            cur+=1
        return end-start+1
    
# Leetcode Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/