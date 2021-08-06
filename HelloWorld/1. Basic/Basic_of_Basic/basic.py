#문자열
print("ㅋ"*3) #ㅋㅋ

#boolean
print(5>10) # = print(False) = print(not True) = print(not (5<10))

#변수형
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "에요")
hobby = "공놀이" #중간에 바꿀 수 있음.
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") #변수형은 문장안에 넣을때 str을 해줘야한다.
# =print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") 위 문장과 같고 변수에 str을 해줄 필요가 없다..그러나 변수+(공백) 이 포함된다.
print(name + "는 어른일까요? " + str(is_adult))

#연산자
print(2**3) # 2^3=8 =3제곱
print(5//3) # 1 =몫

#숫자처리함수

print(abs(-5)) # 5
print(pow(4,2)) # 4^2 = 4*4 = 16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3 반올림
print(round(4.99)) # 5 반올림

from math import *
print(floor(4.99)) # 4 내림
print(ceil(3.14)) # 4 올림
print(sqrt(16)) # 4 루트,제곱근

from random import *
print(random()) #랜덤값 0.0~ 1.0 미만의 임의의 값 생성
print(random() * 10) #랜덤값 0.0~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1~10 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성

print(randrange(1, 46)) #1~46 미만의 임의의 값 생성
print(randint(1, 45)) #1~45 이하의 임의의 값 생성

sentence = '나는 소년입니다' # = "나는 소년입니다"
sentence2 = """나는 소년이고,
파이썬은 쉬워요"""
print(sentence2)

#슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6]) # jumin[0:6]==jum[:6]
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 990120-1234567 에서 맨 마지막자리인 7은 -1번째이다 =jumin[-1] 그러므로 1은 jumin[-7]이다.

#문자열 처리
python = "Python is Amazing!!"
print(python.lower()) # 전부 소문자로 바꾸기
print(python.upper()) # 전부 대문자로 바꾸기
print(python[0].isupper()) # 0번째자리가 대문자인가? True
print(len(python)) #문자열 길이
print(python.replace("Python", "Java")) #Python문자열부분을 Java로 바꾸기
print(python.replace("!", "^-^", 2)) # 3번째 인자 갯수만큼 바꾸어준다. #Python is Amazing^-^^-^
print(python) # 저장은 안됀다.

index = python.index("n") # n은 몇번째에 있을
print(index)
index = python.index("n", index + 1) # n은 몇번째에 있는가 시작위치는 index+1부터이다.
print(index)

print(python.find("Python")) # 있으면 0 없으면 -1
print(python.index("Python")) #  있으면 0 없으면 오류

print(python.count("n")) # n 카운터

#문자열 포멧

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

# 윗문장들은 %c,%d,%s로 맞춰줘야하지만 %s는 다 포함할 수 있다.
print("나는 %s살입니다. " % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", 20))

#다른 방법
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


#다른 방법 2
print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20, color="빨간"))

#다른 방법 3 (v3.6이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


#탈출문자
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

#저는 "나도코딩"입니다. ->  \', \"
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
# \bin\python을 출력하려함
# print("\bin\python") 오류
print("\\bin\\python")

# \r : 커서를 맨 앞으로 이동
print("Red Appleeeeee\rPine A") #Pine A

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

str_="adfwef"
print(str_[1])