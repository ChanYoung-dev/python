# 가장 흔한 단어
# https://leetcode.com/problems/Most_common_Word/
# page.151
import collections
import re

# 내가 푼 문제풀이
'''
from typing import List
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = []
        iter_obj = re.finditer(r'\b(?:\w+)\b', paragraph)
        for obj in iter_obj:
            print(obj.group().lower())
            x = 0
            for i in banned:
                if i == obj.group().lower():
                    print(i, 'vs', obj.group().lower(), '같습니다.')
                    x = 1
                    break
                else:
                    print(i, 'vs', obj.group().lower(), '다릅니다.')

            if x == 0:
                word_list.append(obj.group().lower())

        # 아래는 위와 같은 의미이다.
        #iter_obj = re.finditer(r'\b(?:\w+)\b', paragraph)
        #word = [obj.group().lower() for obj in iter_obj
                #if obj.group().lower() not in banned]
        #print(word)

        word_Count = collections.Counter(word_list)
        print(word_Count)
        return word_Count.most_common(1)[0][0]
'''


# 책에서의 풀이
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = []

        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]
        print(words)

        counts = collections.defaultdict(int)

        for word in words:
            counts[word] += 1
        for key in counts.keys():
            print(key)
        return print(max(counts, key=counts.get))
        # return print(max(counts, key = lambda x : counts[x]))


a = Solution()
print(a.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ["hit"]))