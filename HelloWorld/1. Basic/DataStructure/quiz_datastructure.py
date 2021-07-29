# DataStructure.py에서 배운 것을 토대로 퀴즈풀기
# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
#
# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3: random 모듈의 shuffle과 sample 을 활용
#
# (출력예제)
# --당첨자 발표--
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]
# --축하합니다--

# shuffle은 무작위로 섞는 기능
# sample은 무작위로 n개를 뽑는다
from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # => lst = range(1, 21)
shuffle(lst)
# range를 통해 만들 경우 오류가 뜬다.
# shuffle은 리스트에 대해서만 사용가능, 하지만 range는 리스트형태가 아니다.
# range로 했을 경우 lst = list(lst)로 변환하면 된다.
chick=sample(lst, 1)
print("치킨 당첨자:" + str(chick[0]))
lst.pop(chick[0]) #lst=set(lst)-set(chick)
coffe=sample(lst, 2)
print(coffe)

#다른 방법은 어차피 1+3 =4명이니 4명을 처음부터 뽑는 것이다.
# winner=sample(lst,4)
# print("치킨:".format(winner[0])
# print("치킨:".format(winner[1:])