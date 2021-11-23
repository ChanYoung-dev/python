# p.338
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# DFS
from typing import List
dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(digits) == len(path):
                answer.append(path)

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not (len(digits)):
            return []
        answer = []
        dfs(0, "")
        return answer
a = Solution()
print(a.letterCombinations(digits = "234"))