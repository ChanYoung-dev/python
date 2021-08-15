#내가 한 풀이법 : 속도  68ms
'''
    class Solution:
        # 숫자와 문자 말고는 다 제외한 문자열
        def str_change(self, s: str):
            s_copy = ''
            for i in s:
                if (ord(i) > 64 and ord(i) < 123) or (ord(i) > 47 and ord(i) <58):
                    if ord(i) > 90 and ord(i) < 97:
                        continue
                    else:
                        if ord(i) > 64 and ord(i) < 91:
                            i = i.lower()
                        s_copy += i
            return s_copy
        def isPalindrome(self, s: str) -> bool:
            s_copy = ''
            s_copy = self.str_change(s)
            print(s_copy)
            for i in s:
                if (ord(i) > 64 and ord(i) < 123) or (ord(i) > 47 and ord(i) <58):
                    if ord(i) > 90 and ord(i) < 97:
                        continue
                    else:
                        if ord(i) > 64 and ord(i) < 91:
                            i = i.lower()
                        s_copy += i
            if len(s_copy) == 1:
                return True
            elif len(s_copy) == 2 or len(s_copy) == 3:
                if(s_copy[0] == s_copy[len(s_copy)-1]):
                    return True
                else:
                    return False
            else:
                index = len(s_copy) // 2 - 1 if not len(s_copy) % 2 else len(s_copy) // 2
                if len(s_copy) % 2:
                    if (s_copy[:index+1] == s_copy[:index-1:-1]):
                        return True
                    else:
                        return False
                else:
                    if (s_copy[:index+1] == s_copy[:index:-1]):
                        return True
                    else:
                        return False
a=Solution()
print(a.isPalindrome('race a car'))
'''
#리스트를 이용한 풀이법 : 292 ms
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list=[]
        for char in s:
            if char.isalnum():
                s_list.append(char.lower())
        print(s_list)

        while len(s_list)>1:
            if s_list.pop(0) != s_list.pop():
                return False
        return True

a=Solution()
print(a.isPalindrome('A man, a plan, a canal: Panama'))
'''

#정규식을 이용한 풀이법 : 36ms
'''
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
'''

#데크를 이용한 풀이 : 48ms
import collections
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False
        return True
a=Solution()
print(a.isPalindrome('A man, a plan, a canal: Panama'))

