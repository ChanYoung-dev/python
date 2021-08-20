'''
from typing import List
import re
import collections
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

from typing import List
import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = []

        '''
        words = [word for word in re.sub(r'[^\w]', ' ',paragraph)
                 .lower().split()
                 if word not in banned]
        print(words)
        '''

        iter_obj = re.finditer(r'\b(?:\w+)\b', paragraph)
        words = [obj.group().lower() for obj in iter_obj
                if obj.group().lower() not in banned]
        print(words)
        counts = collections.defaultdict(int)

        for word in words:
            counts[word] += 1
        for key in counts.keys():
            print(key)
        print('count',counts[0])
        print(counts)
        print(max(counts, key = counts.get))
        print(max(counts, key = lambda x : counts[x]))

        nums = [-5, 3, 0, 3, -5]
        print(min(nums, key=lambda x: x % 5))


        menu = {"ham": 1, "cucumber": -12, "egg": 100}

        if menu.get("hame", 5) == 5:
            print("네, 찾는 것이 없네요")
            menu["hame"] = 12
        else:
            print("그런 메뉴는 있습니다.")

        print(menu.get(0))
        #for key in menu.keys():
            #print()

        print(menu.items())

        names = collections.defaultdict(int)
        if names['김찬영']:
            print("김찬영이 있습니다.")
        else:
            print("김찬영이 생성되었습니다..")

        print(names)
a=Solution()
print(a.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ["hit"]))