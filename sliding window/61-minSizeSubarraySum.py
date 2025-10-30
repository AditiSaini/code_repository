class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        combined_nums = [0]
        sum_ = 0
        for i in range(len(nums)):
            sum_+=nums[i]
            combined_nums.append(sum_)
        left = 0
        right = 1
        min_window_size = float('inf')   
        while (left<len(combined_nums)) and (right<len(combined_nums)):
            #Advance right iterator to explore other options
            while (right+1<len(combined_nums)) and combined_nums[right]-combined_nums[left]<target:
                right+=1     
            #Adjust left to min left
            while combined_nums[right] - combined_nums[left] >= target:
                left+=1
            min_window_size = min(min_window_size, right-left+1)   
            right+=1
        if combined_nums[-1] < target:
            return 0
        return min_window_size

# Leetcode Link : https://leetcode.com/problems/minimum-size-subarray-sum/