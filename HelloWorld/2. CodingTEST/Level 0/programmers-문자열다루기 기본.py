import re
class Solution:
    def solutionA(self, s):
        return True if re.search(r'\b\d{4}\b', s) or re.search(r'\b\d{6}\b', s) else False
a = Solution()
print(a.solutionA("123456"))