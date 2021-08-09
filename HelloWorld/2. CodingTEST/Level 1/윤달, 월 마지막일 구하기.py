# 윤년 판단하기

# 윤년 판단 규칙
# 1. 년도가 4로 나누어떨어지는 해는 윤년입니다. (1996년, 2004년, 2008년, 2012년 …)
# 2. 이 중에서 100으로 나누어떨어지는 해는 평년입니다. (1900년, 2100년, 2200년, 2300년 …)
# 3. 그중에 400으로 나누어떨어지는 해는 윤년입니다. (1600년, 2000년, 2400년 …)

while True:
    year = int(input('년도를 입력하시오(0은 종료)'))
    if not year:
        break
    print('윤년' if year%400==0 or year%4==0 and year%100!=0 else '평년')
    # print('윤년' if year%400==0 or year%4==0 and year%100 else '평년')
    # print('윤년' if not year%400 or not year%4 and year%100 else '평년')


# 월을 입력하면 몇일로 구성되어있는지 구하기

# 첫번째 방법
print("첫번째 방법")
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    year = int(input('년도을 입력하시오(0은 종료)'))
    if not year:
        break
    month = int(input('월을 입력하시오(0은종료)'))
    if not month:
        break

    months[1] = 29 if year % 400 == 0 or year % 4 == 0 and year % 100 else 28

    print('{0}년 {1}월의 마지막 날짜는 {2}일 입니다.'.format(year, month, months[month-1]))

# 두번째 방법
print("두번째 방법")
while True:
    year = int(input('년도을 입력하시오(0은 종료)'))
    if not year:
        break
    month = int(input('월을 입력하시오(0은종료)'))
    if not month:
        break

    last_day = (29 if year % 400 == 0 or year % 4 == 0 and year % 100 else 28) \
              if (month==2) else (30 if month%2 else 31) \
              if (month>=8) else (31 if month%2 else 30)

    print('{0}년 {1}월의 마지막 날짜는 {2}일 입니다.'.format(year,month,last_day))


