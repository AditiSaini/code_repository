#Approach 2: Efficient 
class Solution:
    def findAnagrams(self, s, p):
        if len(s)<len(p):
            return []
        elif len(p)==0:
            return [x for x in range(len(s))]
        dict_p = {}
        window = {}
        results = []
        #Dictionary for p 
        for char in p:
            dict_p[char] = dict_p.get(char, 0)+1
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0)+1
            if right-left+1>len(p):
                window[s[left]] = window.get(s[left], 0)-1
                if window[s[left]] == 0:
                    del window[s[left]]
                left+=1
            if window==dict_p:
                results.append(left)
        return results

soln = Solution()
s = "cbaebabacd"
p = "abc"
#s = "abab"
#p = "ab"
print(soln.findAnagrams(s, p))