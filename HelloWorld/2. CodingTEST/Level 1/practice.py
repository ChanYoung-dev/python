from typing import List
import re
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        print(expression)
        if len(expression) == 2:
            return int(expression[0])
            
        for i in range(1, len(expression), 2):
            a = self.diffWaysToCompute(expression[:i])
            b = self.diffWaysToCompute(expression[i+1:])

        if expression[1] == '*':
            return a * b
        elif expression[1] == '+':
            return a + b
        elif expression[1] == '-':
            return a - b
a=Solution()
print(a.diffWaysToCompute(expression = "2*3-4*5"))