# 예외처리

# 구조
'''
try:
    실행 명령문1
    실행 명령문2
    ...
except 에러 종류1:
    예외 처리 명령문1
    예외 처리 명령문2
    ...
except 에러 종류2:
    예외 처리 명령문1
    예외 처리 명령문2
    ...
'''

# 예제
num1 = 6
num2 = 3
print("{0} / {1} = {2} 입니다.".format(num1, num2, int(num1/num2)))
# 6 / 3 = 2 입니다.

#num1 = int(input("1번째 숫자 입력:"))
#num2 = int(input("2번째 숫자 입력:"))
#print("{0} / {1} = {2} 입니다.".format(num1, num2, int(num1/num2)))
# ValueError: invalid literal for int() with base 10: '삼'

# 위 에러를 예외처리하자
'''
try:
    num1 = int(input("1번째 숫자 입력:"))
    num2 = int(input("2번째 숫자 입력:"))
    print("{0} / {1} = {2} 입니다.".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
    '''
'''
1번째 숫자 입력:6
2번째 숫자 입력:삼
잘못된 값을 입력하였습니다.
'''

# 분모에 0을 입력했을때
# ZeroDivisionError: division by zero
'''
try:
    num1 = int(input("1번째 숫자 입력:"))
    num2 = int(input("2번째 숫자 입력:"))
    print("{0} / {1} = {2} 입니다.".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
    '''
'''
1번째 숫자 입력:6
2번째 숫자 입력:0
division by zero # 에러 내용이 뜬다.
'''

# 나머지 모든 에러에 대한 처리
# except Exception as err:
'''
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err: # 나머지 모든 에러에 대한 처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
    '''
'''
나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요 : 10
두 번째 숫자를 입력하세요 : 5
알 수 없는 에러가 발생하였습니다.
list index out of range
'''

# 에러 발생시키기
# raise
# 일부러 에러를 발생시키게 한다.
# 구조
# raise 에러종류
'''
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리수가 아니면 에러 발
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    '''
'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요: 10
두 번째 숫자를 입력하세요: 5
잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.
'''

#사용자 에러처리
# 에러가 발생하였을때 에러 내용을 사용자가 정의할 수 있다
class BigNumberError(Exception): # 사용자 정의 에러
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 사용자가 정의한 자세한 에러 내
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err) # 에러 메시지 출력

'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요: 10
두 번째 숫자를 입력하세요: 5
에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
입력값 : 10, 5
'''


# finally

# 에러가 발생하건 말건 무조건 처리되는 것

# 구조
# try와 except 구문 맨밑
'''
try:
    실행 명령문1
    실행 명령문2
    ...
except 에러 종류1:
    예외 처리 명령문1
    예외 처리 명령문2
    ...
except 에러 종류2:
    예외 처리 명령문1
    예외 처리 명령문2
    ...
finally:
    실행 명령문1
    실행 명령문2
    ...
'''
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: # 에러 발생 여부 상관 없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")

'''
한 자리 숫자 나누기 전용 계산기입니다.
첫 번째 숫자를 입력하세요: 10
두 번째 숫자를 입력하세요: 5
에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
입력값 : 10, 5
계산기를 이용해 주셔서 감사합니다.
'''