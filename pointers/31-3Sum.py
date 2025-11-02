class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i-1>=0 and nums[i-1]==nums[i]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if total>0 and k-1>j:
                    k-=1
                    while nums[k]==nums[k+1] and (k+1)>j:
                        k-=1
                elif total<0 and j+1<k:
                    j+=1
                    while nums[j]==nums[j-1] and (j+1)<k:
                        j+=1
                elif total==0:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplets.append(triplet)
                    if k-1>=0:
                        k-=1
                        while nums[k]==nums[k+1] and k-1>=0:
                            k-=1
                else:
                    break
        return triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    final.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return final 
    
# Leetcode Link : https://leetcode.com/problems/3sum