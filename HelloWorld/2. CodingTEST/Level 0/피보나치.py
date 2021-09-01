# 1 1 2 3 5 8 13 21 34 55 ..
# 앞 두 숫자를 합친 숫자가 계속해서 이어진다.
# 처음 시작부분앞에 0을 넣어주어서
# 0 1 1 2 3 5 8 로 생각해주어서 풀어준다.

count = 0
first = 0
second = 1

while count <= 50:
    print(second, end=' ')
    temp = first # 임시변수
    first = second
    second += temp
    count += 1