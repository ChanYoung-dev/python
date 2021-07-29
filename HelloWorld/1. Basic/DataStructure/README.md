# 자료구조 기본



## 1. 리스트
- ### 선언

```python
->지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)
#[10, 20, 30]

subway = ["유재석", "조세호", "박명수"]

->조세호가 몇번째에 있는가?
print(subway.index("조세호"))
# 1
```

- ### 기능

```python
->하하 추가하기
subway.append("하하")
# ['유재석', '조세호', '박명수', '하하']

->정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1,"정형돈") #첫번째 인수가 몇번째 자리에 넣을 것인가가
# ['유재석', '정형돈', '조세호', '박명수', '하하']

->지하철에 있는 사람을 한 명씩 꺼냄
print(subway.pop())
print(subway)
# 하하
# ['유재석', '정형돈', '조세호', '박명수']

print(subway.pop())
print(subway)
# 박명수
# ['유재석', '정형돈', '조세호']

print(subway.pop())
print(subway)
# 조세
# ['유재석', '정형돈']

->같은 이름의 사람이 몇 명있는지 확인하기
print(subway.count("유재석"))
# 1
```

- ### 정렬


```python
->정렬 sort
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)
# [1, 2, 3, 4, 5]

->순서 뒤집기 가능
num_list.reverse()
print(num_list)
# [5, 4, 3, 2, 1]

->모두 지우기
num_list.clear()
# []

->다양한 자료형 함께 사용
->리스트 합치기/확대
num_list=["조세", 20, True]
# ['조세호', 20, True]
mix_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)

```

## 2. 사전

사전은 key와 valuue의 쌍으로 정의한다
key들은 중복값을 허용하지 않는 유일한 값이다.

- ### 선언

```python
->사전 정의
cabinet = {3 : "유재석", 100: "김태호"}

->값 뽑아내기
print(cabinet[3])
#유재석
```

- ### get

```python
-> get과 위 선언방식의 결과는 같다.
print(cabinet.get(3))
#유재석

->대괄호와 get()의 차이
#print(cabinet(5))
print("hi")

->key가 5인 경우처럼 key값이 없을 땐 에러 발생 후 프로그램 종료(hi출력X)
print(cabinet.get(5))
print("hi")
#key가 5인 경우처럼 key값이 없을 땐 None 반환 후 프로그램 종료(hi출력O)

->get()의 활용
print(cabinet.get(5, "사용 가능"))#key 에 해당하는 값이 없는 경우 기본값을 사용
#사용 가능
```

- ### 기능

```python
->사전 자료형에 값이 있는지 여부확인
print(3 in cabinet) # True
print(5 in cabinet) # False

->key는 정수형이 아닌 문자열도 가능
cabinet={"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"]) #유재석

->업데이트 또는 추가
print(cabinet)
cabinet["A-3"] = "김종국" #key 에 해당하는 값이 있는 경우 업데이트
cabinet["C-20"] = "조세호" #key에 해당하는 값이 없는 경우 신규추가
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

->삭제
del cabinet["A-3"]# {'B-100': '김태호', 'C-20': '조세호'}
```

- ### 출력

```python
->key값들만 출력
print(cabinet.keys())
#dict_keys(['B-100', 'C-20'])

->value들만 출력
print(cabinet.values())
#dict_values(['김태호', '조세호'])

->둘다 확인하기
print(cabinet.items())
#dict_items([('B-100', '김태호'), ('C-20', '조세호')])

->전체삭제
cabinet.clear()
print(cabinet) #{}
```



## 3. 튜플

튜플은 리스트의 '읽기 전용 버전' 느낌이다. 처음 정의할 때를 제외하고는 데이터 변경이나 추가, 삭제 등이 불가능하다.

- ### 선언

```python
->선언 방법 1
menu = ("돈까스", "치즈까스")
print(menu[0]) #돈까스
print(menu[1]) #치즈까스

->선언 방법 2
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
# 김종국 20 코딩

->선언 방법 3
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
# 김종국 20 코딩
```

## 4. 세트
세트는 중복을 허용하지 않으며 또한 데이터의 순서도 보장하지않는다

- ### 선언

```python
->기본 선언
my_set={1, 2, 3, 3, 3}
print(my_set)
# {1, 2, 3}

->set을 이용해 세트 선언
people = set(["유재석","박명수"]) # people = {"유재석", "박명수"}
people2 = {"유재석", "김태호", "양세형"}
```
- ### 기능

```python
->교집합
-> & 기호나 intersection을 이용
print(people & people2) # {'유재석'}
print(people.intersection(people2)) # {'유재석'}

->합집합
-> | 기호나 union()을 이용
print(people | people2) # {'양세형', '김태호', '유재석', '박명수'}
print(people.union(people2)) # {'양세형', '김태호', '유재석', '박명수'}

->차집합
-> - 기호나 difference()를 이용
print(people - people2) # {'박명수'}
print(people.difference(people2)) # {'박명수'}

->추가
people.add("김태호")
print(people) # {'유재석','박명수'} -> {'유재석', '박명수', '김태호'}

->삭제
people2.remove("김태호")
print(people2) # {'유재석', '양세형', '김태호'} -> {'유재석', '양세형'}
```

## 5. 자료구조의 변경
자료구조도 변경이 가능하다
```python
->type 로 어떤 형태인지 확인
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
# {'커피', '주스', '우유'} <class 'set'>

->세트->리스트 변환
menu = list(menu)
print(menu, type(menu))

->튜플로 변환
menu = tuple(menu)
print(menu, type(menu))

->세트로 변환
menu= set(menu)
print(menu, type(menu))
```