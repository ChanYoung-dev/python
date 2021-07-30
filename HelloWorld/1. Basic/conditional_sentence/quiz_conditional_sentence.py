# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#
# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [  ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [  ] 50번째 손님 (소요시간 : 16분)
#
# 총 탑승 승객 : 2 분

# 처음 내가 푼 답
from random import *
sum=0
for i in range(1,51): # 총 탑승 승객 수
    lst=range(5, 51) # 승객당 시간 할당
    lst=list(lst) # list로 변환 / 사실 할 필요없음 shuffle때만 필요
    minute = sample(lst, 1) # lst리스트에서 하나를 뽑아냄
    x=minute[0]
    if x in range(5, 16): #5분이상 15분이하
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, x))
        sum+=1
    else: # 16분이상
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, x))
print(sum)

# 보완해본 내 답
from random import *
sum=0
for i in range(1,51):
    minute = sample(range(5, 51), 1) #range(1,51)=[1,2,3,4,,,,50]이므로 리스트 중 하나를 뽑는 것이다.
    #만약 sample(range(1, 51), 2)이면 두개를 뽑아서 [5,10]으로 저장. 즉, 배열로 저장된다.
    if minute[0] in range(5, 16): #5분이상 15분이하
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, minute[0]))
        sum+=1
    else: # 16분이상
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, minute[0]))
print(sum)

# 문제해답
from random import *

cnt = 0  # 총 탑승 승객 수
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0}분".format(cnt))

# 내 답이랑 차이는 randrange와 sample의 차이다. sample함수를 이해못했으며 sample은 배열내에서의 랜덤 인덱스, randrange는 랜던 숫자이다.