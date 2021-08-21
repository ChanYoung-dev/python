# 로그 파일 재정렬
# https://leetcode.com/problems/reorder-data-in-log-files/
# page.148

# 책에 나온 방법
'''
class Solution
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_split = []
        num_list = []
        letter_list = []
        for log in logs:
            if log.split()[1].isnumeric() == True:
                num_list.append(log)
            else:
                letter_list.append(log)
        letter_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        letter_list.extend(num_list)
        return letter_list
'''

# 정규식을 이용한 방법
from typing import List
import re

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_split = []
        num_list = []
        letter_list = []
        for log in logs:
            if log.split()[1].isnumeric() == True:
                num_list.append(log)
            else:
                letter_list.append(log)
        obj1 = re.compile('(?<=\s).+\Z')
        obj2 = re.compile('\A.+?(?=\s)')
        # ?(?=\s) 에서 맨앞 ?를 붙이는 이유는 나태정량자를 사용하기 위해서다. '.'이 \s공백까지도 먹었기때문이다.

        letter_list.sort(key=lambda x : (obj1.search(x).group(), obj2.search(x).group()))
        letter_list.extend(num_list)
        return letter_list


a = Solution()
print(a.reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))