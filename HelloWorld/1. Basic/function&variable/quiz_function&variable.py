'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오
* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) * 키(m) * 22
여자 : 키(m) * 키(m) * 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm남자의 표준 체중은 67.38kg입니다.
'''

def std_weight(height, gender):
    if gender == "남자":
        weight = height * height * 22 / 10000 # 키가 m이므로 cm로 변환 100*100
    elif gender == "여자":
        weight = height * height * 21 / 10000 # 키가 m이므로 cm로 변환 100*100
    else:
        print("잘못된 입력입니다.")
        weight=0
    return weight

gender = input("성을 입력하세요:")
height = int(input("키를 입력하세요:"))
weight = round(std_weight(height, gender), 2) #소수둘째자리에서 반올림
print("키{0}{1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

'''
성을 입력하세요:남자
키를 입력하세요:175
키175남자의 표준 체중은 67.38kg입니다.
'''