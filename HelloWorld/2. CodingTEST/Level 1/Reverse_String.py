# https://leetcode.com/problems/reverse-string/
# 문자열 뒤집기

# 리턴 없이 내부를 조작할 것

# 내가 푼 풀이
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


a=Solution()
print(a.reverseString(["h", "e", "l", "l", "o"]))


# 주의할 점
# s = s[::-1] 은 되지않는다.
# 그 이유는 새로운 메모리에 s를 할당하는 것으로 인식되기때문이다.

# 불변객체와 가변객체의 차이를 이해해야한다.
# 참고 : 링크

# 내부조작을 위해 다음과 같이 바꾸어준다.
#s[:] = s[::-1]
# 즉, 기존에 선언된 리스트를 바꾸어줄려면 s[:]로 시작해야한다.