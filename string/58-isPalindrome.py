class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        length = len(s)
        right = length - 1
        while left<length and right>=0 and left<right:
            while not(s[left].isalnum()) and left<right:
                left+=1
            while not(s[right].isalnum()) and left<right:
                right-=1
            cur_left = s[left].lower()
            cur_right = s[right].lower()
            if cur_left!=cur_right:
                return False
            left+=1
            right-=1
        return True