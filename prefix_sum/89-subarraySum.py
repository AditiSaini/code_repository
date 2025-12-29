class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0: 1}
        count = total = 0
        for n in nums:
            total+=n
            if total-k in sub_num:
                count+=sub_num[total-k]
            sub_num[total]= sub_num.get(total, 0)+1
        return count