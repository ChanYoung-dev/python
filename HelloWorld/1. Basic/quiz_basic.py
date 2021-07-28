# 기초문법(basic.py)을 배우고 난후 퀴즈
#
# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
#
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성
#
# 예) 생성된 비밀번호 : nav51!

sentence = "http://naver.com"
url = sentence
sentence = sentence[7:sentence.index(".")]
print(sentence) #규칙 1과 2 동시 작업 // 규칙1은 =sentence.replace("http://", "")
password = sentence[:3] + str(len(sentence)) + str(sentence.count("e")) + "!"
print(f"url은 {url}이며, 비밀번호는 {password}입니다.")
print("url은 {1}이며, 비밀번호는 {0}입니다.".format(password, url))
print("url은 %s이며, 비밀번호는 %s입니다."%(url, password))