class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_str = ""
        open_paranthesis_count = 0
        toAdd = []
        for idx in range(len(s)):
            char = s[idx]
            if char == "(":
                open_paranthesis_count+=1
                toAdd.append(len(new_str))
            elif char == ")":
                if open_paratnhesis_count>0:
                    open_paranthesis_count-=1
                    pos = toAdd.pop()
                    new_str = new_str[:pos]+"("+new_str[pos:]
                    new_str+=char
                else:
                    new_str+= ""
            else:
                new_str+=char
        return new_str

#Meta
        