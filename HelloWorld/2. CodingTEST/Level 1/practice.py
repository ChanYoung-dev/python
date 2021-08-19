from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        #불변객체와 가변객체의 차이
        # 가변객체에 같은 값을 주었을때
        print("s1:", s) # ['h', 'e', 'l', 'l', 'o']
        print("s1:", id(s)) # 4302910720

        s = ["h", "e", "l", "l", "o"]
        print("s2", s) # ['h', 'e', 'l', 'l', 'o']
        print("s2:", id(s))  # 4303608160

        s = ["h", "e", "l", "l", "o"]
        print("s3:", s)  # ['h', 'e', 'l', 'l', 'o']
        print("s3:", id(s)) # s: 4389130480
        # 4303818656
        # 같은 값이어도 전부다 다르다

        # 불변객체에 같은 값을 주었을 때

        num = 4
        print("num:", id(num))
        #num: 4541833072
        num = 4
        print("num:", id(num))
        #num: 4541833072
        num2 = 4
        print("num2:", id(num2))
        #num2: 4509069168

        str_num = '123'
        print("str_num:", id(str_num))
        # str_num: 4516378672
        str_num = '123'
        print("str_num:", id(str_num))
        # str_num: 4516378672
        str_num2 = '123'
        print("str_num2:", id(str_num2))
        # str_num: 4516378672
        # 같은값이면 주소가 전부 같다.


        # 가변객체와 불변객체의 같은점

        # 가변객체 = 가변객체
        str_list = ["a", "b", "c"]
        print("str_list:", id(str_list)) # str_list: 4388907600
        s = str_list
        print("copy_str_list:", id(str_list)) # copy_str_list: 4388907600
        print("copy_s: ", id(s)) # copy_s:  4388907600


        # 불변객체 = 불변객체
        num = 3
        print("num:", num)
        print("num(id):", id(num))
        num2 = 1
        print("num2:", num2)
        print("num2(id):", id(num2))

        num2 = num
        print("num2:", num2)
        print("num2(id):", id(num2))

        #가변객체의 내부조작
        s = ["h", "e", "l", "l", "o"]
        print(id(s))
        s[0] = "e"
        print("s:", s)
        print(id(s))

        #불변객체의 내부조작
        s = "hellow"
        print(id(s))
        s[3] = "e"
        print("s:", s)
        print(id(s))
        #오류가 뜬다



a=Solution()
print(a.reverseString(["h", "e", "l", "l", "o"]))

