class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)-1
        closest = float('inf')
        closest_sum = 0
        for i in range(len(nums)):
            current = nums[i]
            start = i+1
            end = size
            while start<end:
                current_sum = current + nums[start] + nums[end]
                diff = current_sum-target
                if abs(diff)<closest:
                    closest = abs(diff)
                    closest_sum = current_sum
                if diff>0:
                    end-=1
                elif diff<0:
                    start+=1
                elif diff==0:
                    return current_sum
        return closest_sum