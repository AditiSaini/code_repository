import math 
class Solution:
    def myAtoi(self, s: str) -> int:
        count = 0
        val = 0
        digit = ['0','1','2','3','4','5','6','7','8','9']
        sign = 1
        sign_observed = False
        first_digit = False
        while count<len(s):
            char = s[count]
            if char == "-" and not(first_digit) and not(sign_observed):
                sign_observed = True
                sign = -1
            elif char == "+" and not(first_digit) and not(sign_observed):
                sign_observed = True
                sign = 1
            elif char in [' ', '+', '-'] and (first_digit or sign_observed):
                break
            elif char!= '0' and (char not in digit) and (char != ' '):
                break
            elif char in digit:
                first_digit = True
                val = val*math.pow(10, 1) + int(char)
            count+=1
        val *= sign
        val = int(min(max(math.pow(-2, 31), val), math.pow(2, 31) - 1))
        return val

# Leetcode Link: https://leetcode.com/problems/string-to-integer-atoi/