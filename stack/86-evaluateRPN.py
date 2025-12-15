class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set(['+', '-', '*', '/'])
        for token in tokens:
            if (token.isnumeric()) or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            elif token in operator:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    result = num1+num2
                elif token == '-':
                    result = num1-num2
                elif token == '*':
                    result = num1*num2
                elif token == '/':
                    result = int(num1/num2)
                stack.append(result)
        return stack[0]

# Leetcode Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/