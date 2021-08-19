# 1. 불변/가변 객체
## 1. 불변과 가변의 차이
### 같은 데이터가 주었을때
#### 가변객체 같은 데이터 선언


s = ["h", "e", "l", "l", "o"]
print("s2", s)  # ['h', 'e', 'l', 'l', 'o']
print("s2의 id:", id(s))  # s2: 4407217216

s = ["h", "e", "l", "l", "o"]
print("s3:", s)  # ['h', 'e', 'l', 'l', 'o']
print("s3의 id:", id(s))  # s3: 4407888384

'''
같은
값이어도
전부다
다르다
'''
### 불변객체 같은 데이터 선언
#### 숫자

num = 4
print("num:", id(num))
# num: 4405852560
num = 4
print("num:", id(num))
# num: 4405852560
num2 = 4
print("num2:", id(num2))
# num2: 4405852560

####문자열

str_num = '123'
print("str_num:", id(str_num))
# str_num: 4407889520
str_num = '123'
print("str_num:", id(str_num))
# str_num: 4407889520
str_num2 = '123'
print("str_num2:", id(str_num2))
# str_num2: 4407889520
'''
같은값이면
주소가
전부
같다.
'''
### 객체의 내부조작
#### 가변객체의 내부조작

s = ["h", "e", "l", "l", "o"]
print(id(s))
# s의 id :4407217216
s[0] = "e"
print("s:", s)
#s: ['e', 'e', 'l', 'l', 'o']
print(id(s))
# s의 id :4407217216

#### 불변객체의 내부조작

s = "hellow"
print(id(s))
# 4407910576
# s[3] = "e" # 오류발생
print("s:", s)
# s: hellow
print(id(s))
# s : 4407910576
'''
오류가
뜬다
'''
## 2. 가변객체와 불변객체의 공통점

### 가변객체 = 가변객체

s = ["h", "e", "l", "l", "o"]
print("s:", id(s))
# s: 4407217216
str_list = ["a", "b", "c"]
print("str_list:", id(str_list))
# str_list: 4407888384
s = str_list
print("copy_str_list:", id(str_list))
# copy_str_list: 4407888384
print("copy_s: ", id(s))
# copy_s:  4407888384

### 불변객체 = 불변객체
num = 3
print("num:", num)
print("num(id):", id(num))
#num: 3
#num(id): 4405852528


num2 = 1
print("num2:", num2)
print("num2(id):", id(num2))
#num2: 1
#num2(id): 4405852464


num2 = num
print("num2:", num2)
print("num2(id):", id(num2))

#num2: 3
#num2(id): 4405852528
