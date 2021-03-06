# 모듈
# theater_module.py 파일에 있는 함수들을 사용해보자
# import 방법1

import theater_module
theater_module.price(3)
theater_module.price_morning(3)
theater_module.price_soldier(3)
'''
3 명의 가격은 30000원입니다.
3명의 가격은 18000입니다
3명의 가격은 12000입니다
'''

# import 방법2
import theater_module as mv
mv.price(3)
mv.price_morning(3)
mv.price_soldier(3)

'''
3 명의 가격은 30000원입니다.
3명의 가격은 18000입니다
3명의 가격은 12000입니다
'''

# from ~ import 구문
# 모듈내 모든 것을 가져다가 사용하겠다.
from theater_module import *
price(3)
price_morning(3)
price_soldier(3)
'''
3 명의 가격은 30000원입니다.
3명의 가격은 18000입니다
3명의 가격은 12000입니다
'''

# 모듈내 필요한 것만 사용하겠다.
from theater_module import price, price_morning
price(3)
price_morning(3)
price_soldier(3)
#NameError: name 'price_soldier' is not defined


# from ~ import ~ as ~
# 필요한 함수를 줄임말로 사용한다

from theater_module import price_soldier as price # price_soldier가 새로운 별명인 price 사용
price(3)
# 3명의 가격은 12000입니다

# 패키지
# 여러 모듈을 모아 놓은 집합
# travel패키지의 thailand 모듈 사용
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

# import로 직접 클래스나 함수 import는 불가능
#import travel.thailand.ThailandPackage # 클래스 직접 import 불가
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
#ModuleNotFoundError: No module named 'travel.thailand.ThailandPackage'; 'travel.thailand' is not a package

# from ~ import ~ 는 클래스나 함수 바로 import가
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원


from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# [베트남 패키지 3박 5일] 다낭 효도 여행 60만원


# __all__
# from random import *
# random 모듈을 import 함으로써 random 모듈 내의 모든 것을 가져다 쓴다.

# 그렇다면 앞선 travl도 적용해보자
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
# NameError: name 'vietanm' is not defined
# why? 공개설정을 해야된다.
# travel/__init__.py 파일 수정
# __all__ = ["vietanm"] # vietnam 모듈 공개

# 다시 실행하면
# [베트남 패키지 3박 5일] 다낭 효도 여행 60만원
# 성공적으로 잘 나타난다.

# 모듈 직접 실행
# 모듈이 외부에서 호출되어 실행하는지 직접 실행하는지 확인하기
# thailand.py에서 다음과 같은 코드 추가
'''
if __name__ == "__main__": # 모듈이 직접 실행되는 경우 
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else: # 외부에서 모듈 호출되는 경우 
    print("Thailand 외부에서 모듈 호출")
'''

# 처음 import 할때만 어디서 호출이 됐는지 뜬다.
from travel import *
trip_to = thailand.ThailandPackage()
# 이 때 'Thailand 외부에서 모듈 호출' 출력
# 이 이후로는 thailand를 import 선언해도 이미 선언했기때문에 안 뜬다.
trip_to.detail()
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

# 패키지, 모듈위치
# inspect
# 패키지나 모듈의 경로 확인
import inspect
import random
print(inspect.getfile(random))
# /usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/random.py

# random 모듈이 있는 lib폴더에 내가 만들어 놓은 travel패키지를 붙여넣으면
# 같은 경로가 아니더라도 어디서든지 호출을 할수 있다.


# pip install
# 유용한 패키지 사용
# 파이썬은 유용한 패키지가 많다. 그 패키지를 찾는 방법 중 하나는 https://pypi.org 사이트이다.


# 패키지 중 웹스크래핑에서의 대표적인 beautifulsoup 패키지를 사용해보
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
'''
# 경고 메세지는 무시해도 좋다. 설치방법을 알기 위한 것일 뿐

# pip의 여러가지 명령어


# 내장함수
# 별도로 import를 하지 않고도 사용할 수 있도록 내장되어 있는 함수
# ex) input,upper 등등

# dir() 어떤 객체가 매개변수로 들어갔을때 어떤 변수와 함수를 갖고있는지를 알려준다
# 매개변수가 없을 경우 소스코드 범위내에 사용가능한 모듈 또는 객체가 출력된다.

print(dir())
# ['ThailandPackage', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'inspect', 'mv', 'price', 'price_morning', 'price_soldier', 'random', 'thailand', 'theater_module', 'travel', 'trip_to', 'vietnam']
import pickle
print(dir())
# ['ThailandPackage', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'inspect', 'mv', 'price', 'price_morning', 'price_soldier', 'random', 'thailand', 'theater_module', 'travel', 'trip_to', 'vietnam']
# pickle이 추가된것을 확인할 수 있다.

# random모듈을 직접 전달값으로 설정
print(dir(random))
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
# randint, randrange, sample, shuffle등 확인 가능

# 모듈이 아닌 리스트를 확읺해보자
lst = [1,2,3]
print(dir(lst))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# append, clear, count, extend, index, reverse, sort 등을 확인 가능

name = "Jim"
print(dir(name))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# upper, lower, find 등 다양한 기능 확인할수있따.

# 더 자세한 내장함수에 대한 내용은 list of python builtins 검색


# 외장함수
# 외장함수는 내장함수와는 다르게 반드시 import를 해야한다. ex)random
# list of python modules 검색
# 대표적인 외장함수를 보자
# glob
# 어떤 경로 내의 폴더 또는 파일의 목록을 조회할 때 사용하며 윈도우에서의 dir명령이다.
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일을 조회

# ['module.py', 'theater_module.py']

# os
# 운영체제에서 제공하는 기본 기능 느낌
# getcwd
# 현재 작업 디렉토리 의미, cwd란 current working directory
import os
print(os.getcwd()) # 현재 디렉토리
#/Users/gimchan-yeong/PycharmProjects/HelloWorld/1. Basic/Module

# path.exists 매개변수와 동일한 이름의 폴더가 존재하는지 확인
# makedirs 새로운 폴더 생성
# rm 삭제
import os
folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다. ")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생상하였습니다.")

# 처음 실행시 sample_dir폴더 생기는 것을 확인할 수 있다.

#listdir()
# ls와 비슷한 기능
import os
print(os.listdir())
# ['__pycache__', 'sample_dir', 'module.py', 'travel', 'theater_module.py']

#time
# 현재시간정보 확인 localtime()
import time
print(time.localtime())
# time.struct_time(tm_year=2021, tm_mon=8, tm_mday=5, tm_hour=19, tm_min=46, tm_sec=23, tm_wday=3, tm_yday=217, tm_isdst=0)
# 알아보기가 힘들다

# strftime()
# 문자열형태로 나타내기
print(time.strftime("%Y-%m-%d %H:%M:%S"))
#2021-08-05 19:48:01

#datetime
# 오늘 날짜출력
import datetime
print("오늘 날짜는", datetime.date.today())
#오늘 날짜는 2021-08-05

#timedelta
# 일수를 저장한다. 디데이에 유용
import datetime
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후


