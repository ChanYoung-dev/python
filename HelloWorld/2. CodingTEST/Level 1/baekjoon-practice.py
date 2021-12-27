import re
class Solution:
    def solution(self):
        data =int(input())
        i = 0
        result = 0
        while True:
            result += i
            if result == data:
                return i
            elif result > data:
                return i-1
            i += 1



a=Solution()
print(a.solution())
#그리드