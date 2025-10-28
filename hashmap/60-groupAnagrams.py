class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hashmap = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_hashmap:
                anagram_hashmap[sorted_word].append(word)
            else:
                anagram_hashmap[sorted_word]=[word]
        all_anagrams = [val for key, val in anagram_hashmap.items()]
        return all_anagrams
    
# Leetcode Link: https://leetcode.com/problems/group-anagrams/