class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = set(['{', '(', '['])
        stack = []
        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            elif len(stack)>0:
                if ch == '}' and stack.pop()!='{':
                    return False
                elif ch == ')' and stack.pop()!='(':
                    return False
                elif ch == ']' and stack.pop()!='[':
                    return False
            else:
                return False
        if len(stack)==0:
            return True 
        return False

# Leetcode Link : https://leetcode.com/problems/valid-parentheses/