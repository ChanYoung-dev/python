# if
# 인덴트(indent) : if 조건에 만족할 때 실행해야 하는 문장들은 if위치 기준으로 스페이스4칸씩 들여쓰기를 해야한다.

#elif=else if
weather = "미세먼지"

if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

# cf)input응용
# input은 입력받는 것이다. 항상 "문자열"로 입력받기때문에, 숫자 3을 입력해도 문자열 "3"으로 인식한다.
weather = input("오늘 날씨 어때요? ")
print(weather)
# 오늘 날씨 어때요? '좋아' (입력시)
# 좋아

#if문 and나 or 연산자 응용
temp = int(input("기온은 어때요? ")) #문자열인식 받는 것을 정수형으로 변환
if 30 <=temp: #30도이상
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # 10도 이상 30도 미만
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
# 위 비교 문장은
# elif 0 <= temp < 10:
# 과 같다.
    print("외투를 챙기세요")
else: # 그 외의 모든 경우
    print("너무 춥다")


#for

'''
for 변수 in 반복대상:
    실행 명령문1
    실행 명령문2
'''

# 기본
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))
'''
대기번호 : 1
대기번호 : 2
대기번호 : 3
대기번호 : 4
'''
# 반복이 많을땐?
# range 이용
for waiting_no in range(1, 5):
    print("대기번호 : {0}".format(waiting_no))
'''
대기번호 : 1
대기번호 : 2
대기번호 : 3
대기번호 : 4
'''
# 배열(리스트) 응용
hero = ["아이언맨", "토르", "아이엠 그루트"]
for customer in hero:
    print("{0}님 커피가 준비되었습니다.".format(customer))
'''
아이언맨님 커피가 준비되었습니다.
토르님 커피가 준비되었습니다.
아이엠 그루트님 커피가 준비되었습니다.
'''

#while
'''
while 조건:
    실행 명령문1
    실행 명령문2
    실행 명령문3
'''

#기본
customer = "토르"
index = 5

while index>=1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -=1
    if index == 0:
        print("커피는 폐기 처분되었습니다.")
'''
토르, 커피가 준비 되었습니다. 5번 남았어요.
토르, 커피가 준비 되었습니다. 4번 남았어요.
토르, 커피가 준비 되었습니다. 3번 남았어요.
토르, 커피가 준비 되었습니다. 2번 남았어요.
토르, 커피가 준비 되었습니다. 1번 남았어요.
커피는 폐기 처분되었습니다.
'''

#활용
customer = "토르"
person = "Unknown"

while customer != person:
    print("{0}님 커피 준비됐습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
'''
{0}님 커피 준비됐습니다.
이름이 어떻게 되세요?아이언맨
{0}님 커피 준비됐습니다.
이름이 어떻게 되세요?아이엠 그루트
{0}님 커피 준비됐습니다.
이름이 어떻게 되세요?토르
'''


#continue,break

#continue
absent = [2, 5]

for student in range(1,11):
    if student in absent: # 결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
        continue
    print("{0}번 책읽으세요.".format(student)) # 반복문
'''
1번 책읽으세요.
3번 책읽으세요.
4번 책읽으세요.
6번 책읽으세요.
7번 책읽으세요.
8번 책읽으세요.
9번 책읽으세요.
10번 책읽으세요.
'''

#break
absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent: # 결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
        continue
    elif student in no_book: # 책을 가져오지 않았으면 바로 수업 종료 (반복문 탈출)
        print("오늘 수업 여기까지. {0}번은 교무실로 따라와".format(student))
        break
    print("{0}번 책을 읽으세요".format(student)) # 반복문

'''
1번 책을 읽으세요
3번 책을 읽으세요
4번 책을 읽으세요
6번 책을 읽으세요
오늘 수업 여기까지. 7번은 교무실로 따라와
'''

#한 줄 for
# 기본
# 변수로 어떤 동작 for 변수 in 반복대상
students =[1, 2, 3, 4, 5]
print(students)
#[1, 2, 3, 4, 5]
students = [i + 100 for i in students] # i를 뽑아서 100에 각각 더
# students = [students[0] + 100, students[1] + 100, students[2] + 100, students[3] + 100, students[4] + 100]
print(students)
# [101, 102, 103, 104, 105]

#활용
students = ["김", "김찬", "김찬영"]
lens = [len(i) for i in students]
print(lens)
#[1, 2, 3]

#대문자로 바꾸
students = ["a", "bc", "de f"]
students = [i.upper() for i in students]
print(students)
#['A', 'BC', 'DE F']

# 3중 if문
a=1
b=2
print("같다" if a==b else "틀리다")
# 같다

# 윤년 판단 규칙
# 1. 년도가 4로 나누어떨어지는 해는 윤년입니다. (1996년, 2004년, 2008년, 2012년 …)
# 2. 이 중에서 100으로 나누어떨어지는 해는 평년입니다. (1900년, 2100년, 2200년, 2300년 …)
# 3. 그중에 400으로 나누어떨어지는 해는 윤년입니다. (1600년, 2000년, 2400년 …)

while True:
    year = int(input('년도를 입력하시오(0은 종료)'))
    if not year:
        break
    # print('윤년' if year%400==0 or year%4==0 and year%100!=0 else '평년')
    # print('윤년' if year%400==0 or year%4==0 and year%100 else '평년')
    print('윤년' if not year%400 or not year%4 and year%100 else '평년')


# assert
# 디버깅용도a = 10
#assert a > 5
#assert a < 5
# AssertionError
#assert a < 5, "a의 값이 너무 큽니다."
# AssertionError: a의 값이 너무 큽니다.

#map
def plus_two(x):
    return x+2

a = list(map(plus_two, [1, 2, 3, 4]))
print(a) # [3, 4, 5, 6]
a = list(map(lambda a:a+2, [1, 2, 3, 4]))
print(a) # [3, 4, 5, 6]
a = [a+2 for a in range(1,5)]
print(a) # [3, 4, 5, 6]
