# 파이썬 문법
## 인덴트

'''
인덴트는 공백 4칸이다. 하지만 우리는 pyCharm을 이용하여 인덴트에 신경을 안쓰고 개발할 수 있다.
설마 잘못입력하더라도 pycharm에서 Reformat Code를 실행하면 된다.
'''

## 네이밍 컨벤션
'''
변수나 함수이름을 짓는 방식이다.
카멜케이스 = camelCase
스네이크케이스 = snake_case
파스칼케이스 = CameCase
'''

## 타입 힌트

'''
동적인 파이썬에 정적인 기능을 넣은 
def fn(a)
 빠르게 정의해서 사용할수 있다는 장점이 있지만 어떤 식으로 파라미터를 넘기고 무슨 리턴값이 나오는지를 알 수가 없다.
def fn(a: int) -> bool:
파라미터가 정수형인 것과 리턴 값으로 True or False를 반환하는 것도 알수 있다.것

a: str = "1"
b: int = 1
선언할 수 있는 타입을 잘 명시할 수 있다.

하지만, 여전히 동적인 파이썬이므로 실제 문자열형에 정수형 변수를 대입한다해도 오류는 뜨지 않는다.
a: str = 1 
# 오류는 나타나지않는다

하지만 mypy를 사용하면 확인할 수 있다.
pip install mypy 로 mypy를 설치한 뒤,
mypy 파일명.py 를 하면 된다.
'''

##  Comprehension
#코드를 더 단순화 할수 있다.
### List Comprehension Code
list_comprehension = [ n * 2 for n in range(1, 10+1) if not n%2]
print(list_comprehension)
# [4, 8, 12, 16, 20]

### No List Comprehension Code
no_list_comprehension = []
for n in range(1, 10+1):
    if n % 2 == 0:
        no_list_comprehension.append(n*2)

print(no_list_comprehension)
# [4, 8, 12, 16, 20]

### no_Dictionary Comprehension Code
original = {"나": "김찬영", "친구": "강민숙"}

no_dict_comprehension = {}
for key, value in original.items():
    no_dict_comprehension[key] = value
print(original)
print(no_dict_comprehension)
#{'나': '김찬영', '친구': '강민숙'}

### Dictionary Comprehension Code
dict_comprehension = {key: value for key, value in original.items()}
print(dict_comprehension)
#{'나': '김찬영', '친구': '강민숙'}


## generator
#루프의 반복(iteration)동작을 제어할 수 있는 루틴형태.
#iterator는 클래스에 __iter__, __next__ 또는 __getitem__ method를 구현해야 하지만
#제너레이터는 yield만 사용하면 된다.
def number_generator():
    yield 0
    yield 1
    yield 2

print(number_generator())
ng= number_generator()

'''
for i in ng:
    print(i, end=' ')
# 0 1 2 
'''

#next는 추출이다.
print(next(ng))
# 0
print(next(ng))
# 1
print(next(ng))
# 2
#print(next(ng))
# Error : StopIteration

## range
#generator를 활용하는 대표적인 함수
range_a = [n for n in range(100)]
range_b = range(0, 100+1)
#모든것이 다 똑같지만 메모리차지 크기가 다르다.
print(range_a)
# [0, 1, 2, 3, 4, 5,...,100]
# 메모리점유율 엄청 높다
print(range_b)
# range(0, 101)
# 메모리점유율 엄청 낮다.

## enmerate
#여러가지 자료형을 인덱스를 포함한 enmerate 객체로 리턴한다.

enum = [1, 2, 3]
print(list(enumerate(enum)))
# [(0, 1), (1, 2), (2, 3)]

for i, v in enumerate(enum):
    print(i, v)
'''
0 1
1 2
2 3
'''

## locals
#사용되는 지역변수 조회
#디버깅에 필요하다
#함수 내부의 지역 정보를 조회해 잘못 선언한 부분이 없는지 확인하는 용도
def local_function():
    local_a = 1
    local_b = 2
    print(locals())


local_function()
print(locals())
'''
'__name__': '__main__', '__doc__': '\n인덴트는 공백 4칸이다. 하지만 우리는 pyCharm을 이용하여 인덴트에 신경을 안쓰고 개발할 수 있다.\n설마 잘못입력하더라도 pycharm에서 Reformat Code를 실행하면 된다.\n',\
 '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x102215490>,\
  '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,\
   '__file__': '/Users/gimchan-yeong/PycharmProjects/HelloWorld/3. Coding Interview/python.py',\
    '__cached__': None, 'list_comprehension': [4, 8, 12, 16, 20], 'no_list_comprehension': [4, 8, 12, 16, 20],\
     'n': 10, 'original': {'나': '김찬영', '친구': '강민숙'}, 'no_dict_comprehension': {'나': '김찬영', '친구': '강민숙'},\
      'key': '친구', 'value': '강민숙', 'dict_comprehension': {'나': '김찬영', '친구': '강민숙'},\
       'number_generator': <function number_generator at 0x102268cb0>, 'ng': <generator object number_generator at 0x102248cd0>,\
        'range_a': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\
         51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],\
         'range_b': range(0, 101), 'enum': [1, 2, 3], 'i': 2, 'v': 3, 'local_function': <function local_function at 0x102268d40>}

local_a와 local_b가 없다. -> 지역변수이기때문
'''