class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = defaultdict(int)
        for char in s:
            store[char]+=1
        for char in t:
            if char in store and store[char]>0:
                store[char]-=1
                if store[char]==0:
                    del store[char]
            else:
                return False
        if len(store)>0:
            return False
        return True
    
# Leetcode Link : https://leetcode.com/problems/valid-anagram/