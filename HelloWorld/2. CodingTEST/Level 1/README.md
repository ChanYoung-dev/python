dict 정리

#1. 키 값 대입
- ## get 사용시
>menu.get()은 맞을시 True,
아닐시 None을 뱉는다.
```python
menu = {"ham": 1, "cucumber": -12, "egg": 100}

if menu.get("hame"):
    print("네, 찾는 것이 있네요")
    menu["hame"] = 12
else:
    print("그런 메뉴는 없습니다.")
print(menu.items())
#dict_items([('ham', 1), ('cucumber', -12), ('egg', 100), ('hame', 12)])
```


get두번째인자에 넣으면
```python
if menu.get("hame", 5) == 5:
    print("네, 찾는 것이 없네요")
else:
    print("그런 메뉴는 있습니다.")
```
없을시 5가 출력된다.  
생성되는 것이 아니라 5를 호출한다.

- ## defaultdict 사용
라이브러리를 사용하여 손쉽게 만드는법
```python
names = collections.defaultdict(int)
        if names['김찬영']:
            print("김찬영이 있습니다.")
        else:
            print("김찬영이 생성되었습니다..")

        print(names)
```


print(max(counts, key = counts.get))
print(max(counts, key = lambda x : counts[x]))
같은 뜻이다.