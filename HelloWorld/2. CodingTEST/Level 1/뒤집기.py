import re
class Solution:
    def solution(self, data):
        return (min(len(re.findall('1+', data)), len(re.findall('0+', data))))
a=Solution()
print(a.solution('11111'))
#그리드