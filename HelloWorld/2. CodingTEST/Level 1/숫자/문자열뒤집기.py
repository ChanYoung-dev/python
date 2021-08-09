# 정수형을 문자열로 변환
# 문자열을 리스트로 변환
# 리스트를 거꾸로 정렬
# 리스트를 문자열로 반환
num = 123456
print("num:{0}".format(num))  # 123456

str_num = str(num)  # 문자열 변환
print("str_num:{0},type: {1}, str_num[0] : {2} ".format(str_num, type(str_num), str_num[0]))
# str_num:123456,type: <class 'str'>, str_num[0] : 1

str_list = list(str_num)  # 문자열을 리스트로 변환
str_list.reverse()  # reverse는 리스트에서만 사용할 수 있기때문에 리스트로 변환해준다
print("str_list(reverse)  : {0} type: {1}".format(str_list, type(str_list)))
# str_list(reverse)  : ['6', '5', '4', '3', '2', '1'] type: <class 'list'>

str_list = ''.join(str_list)  # 리스트에서 문자열로 변환해준다.
print("str_list(reverse)  : {0} type: {1}".format(str_list, type(str_list)))
# str_list(reverse)  : 654321 type: <class 'str'>