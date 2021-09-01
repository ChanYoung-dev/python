name = ["찬영", "민수", "지언", "성우"]

while True:
    what_name=input("찾는 사람의 이름은?")
    if what_name =='': # 엔터를 입력시 탈출
        break
    print('회원' if what_name in name else '손님','입니다',sep='')