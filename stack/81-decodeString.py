class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                cur_string = ""
                #Pop the stack until I find an opening bracket
                while len(stack)>0:
                    if stack[-1]!='[':
                        cur = stack.pop()
                        cur_string = cur + cur_string
                    else:
                        break
                #Removes opening bracket
                stack.pop()
                #Pop the stack to extract the entire number
                num = ""
                while len(stack)>0:
                    if stack[-1].isdigit():
                        num = stack.pop() + num
                    else:
                        break
                cur_string = int(num)*cur_string
                stack.append(cur_string)
        return ''.join(stack)

# Leetcode Link : https://leetcode.com/problems/decode-string