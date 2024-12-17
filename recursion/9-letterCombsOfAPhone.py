from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        all_combs = []
        digit_dict = {'2':'abc', '3':'def', '4':'ghi', 
        '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        orig_digit_length = len(digits)
        def recurse_comb(digits, current_permute):
            if len(current_permute)==orig_digit_length:
                all_combs.append(current_permute)
                return 
            for id_ in range(len(digits)):
                alphas = digit_dict[digits[id_]]
                for idx in range(len(alphas)):
                    char = alphas[idx]
                    recurse_comb(digits[id_+1:], current_permute+char)
        if len(digits)!=0:
            recurse_comb(digits, '')
        return all_combs

s = Solution()
print(s.letterCombinations('23'))