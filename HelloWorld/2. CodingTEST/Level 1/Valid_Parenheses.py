# 유효한 괄호
# https://leetcode.com/problems/valid-parentheses/
# page.245


class Solution:
    def isValid(self, s: str) -> bool:
        # 거꾸로 문자열정렬하기
        s_copy=s[::-1]
        table = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }

        stack_parentheses = []
        for char in s_copy:
            print("char", char)
            if char not in table:
                stack_parentheses.append(char)
            else:
                if len(stack_parentheses) == 0 or (table[char] != stack_parentheses.pop()):
                    return False

        if len(stack_parentheses) != 0:
            print("스택이 남아있습니다.", stack_parentheses)
            return False
        else:
            return True




print(Solution().isValid("{[]}"))

