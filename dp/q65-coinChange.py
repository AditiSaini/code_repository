class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        minAmt = [float('inf')]* (amount+1)
        minAmt[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c<=i:
                    minAmt[i] = min(minAmt[i], minAmt[i-c]+1)
        result = minAmt[-1]
        if result==float('inf'):
            return -1
        return result

# Leetcode Link : https://leetcode.com/problems/coin-change