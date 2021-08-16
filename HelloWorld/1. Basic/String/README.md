# 1. 슬라이싱
```python
s = 'hellow'
print(s[1:4]) #ell / index1부터 4-1 까지 출력
print(s[1:-2]) #ell / index1부터 뒤에서2번째이전까지 출력 / 뒤에서 1번째가 인덱스 -1이다.
print(s[:]) # hellow /복사가 된다. 이때 참조가 아닌 값 복사이다. 
# list같은경우에 유용하다. 왜냐하면 list는 가변객체이기때문에 참조하기 때문이다.
print(s[1]) # e
print(s[::-1]) #wolleh
print(s[::2]) #hlo
```
# 2. 정규표현식(re)
> 특정 문자를 찾거나 찾은 문자를 다른 문자로 대체해주는 등 문자열 조작방법 중 하나

## 1. 메타문자
**` $()*+.?[\^{**
>기능을 갖은 문자이다.  
>이 문자를 찾고 싶으면 백슬래시(\)를 붙여주자 아니면 대괄호 안에 넣어도 된다.
## 2. import
```python
import re
```

## 3. re의 함수
- ### re.match
> 문자열의 "처음"부터 시작하여 패턴을 찾는다.
```python
s = 'hellow'
print(re.match('h', s)) # <re.Match object; span=(0, 1), match='h'>
print(re.match('e', s)) # None
```
>h가 처음부터 있으므로 span=(0,1)을 통해 h의 위치인 0부터 1이전(즉,0)을 확인할수 있다.  
e는 hellow안에 있지만 처음부터 없으므로 X

- ### re.search
> 특정패턴문자가 문자열안에 있는지
```python
print(re.search('h', s)) # <re.Match object; span=(0, 1), match='h'>
print(re.search('e', s)) # <re.Match object; span=(1, 2), match='e'>
```

- ### re.findall
> 패턴과 일치하는 모든 부분을 찾아낸다.
```python
print(re.findall('h', s)) # ['h']
print(re.findall('l', s)) # ['l', 'l']
print(re.findall('z', s)) # []
_s = 'hhhh'
print(re.findall('hhh', _s)) # ['hhh']
# 'hhhh' 에서 index0~2인 hhh와 index1~3인 hhh가 있지만 overlapping을 하지않는다.
```

- ### re.finditer
  > findall과 비슷하지만 Iterator형식으로 패턴 찾은 것을 보여준다.
```python
finditer_obj = re.finditer('h', s)
for obj in finditer_obj:
print(obj)
# <re.Match object; span=(0, 1), match='h'>

finditer_obj = re.finditer('hhh', _s)
for obj in finditer_obj:
    print(obj)
# <re.Match object; span=(0, 3), match='hhh'>

finditer_obj = re.finditer('l', s)
for obj in finditer_obj:
    print(obj)
# <re.Match object; span=(2, 3), match='l'>
# <re.Match object; span=(3, 4), match='l'>
```
- ### re.fullmatch
> 완벽하게 같은 문자열패턴을 찾아준다.
```python
print(re.fullmatch('h', s)) # None
print(re.fullmatch('hell', s)) # None
print(re.fullmatch('hellow', s)) # <re.Match object; span=(0, 6), match='hellow'>
```
- ### match_object의 method
#### *group(), start(), end(), span()*
```python
match_Object = re.search('l', s)
print(match_Object) # <re.Match object; span=(2, 3), match='l'>
print(match_Object.group()) # l 일치한 문자열패턴 반환
print(match_Object.start()) # 2 일치한 문자열 시작위치
print(match_Object.end()) # 3 일치한 문자열 끝 위치
print(match_Object.span()) # (2, 3) 일치한 문자열의 시작,끝 튜플로 반환
```

## 4.정규식 자료
- ### 대괄호
    > [abcd] == [ a or b or c or d ]  
    > a나 b나 c나 d 중 하나라도 들어가있는지
    ```python
    print(re.search('[zh]', s)) # <re.Match object; span=(0, 1), match='h'>
    # z나 h가 들어가면 출력  -> h가 들어갔으므로 출력
    print(re.search('he[zl]', s)) # <re.Match object; span=(0, 3), match='hel'>
    #hez 나 hel 일 경우 출력
    ```
    
    - #### -
    >-는 메타문자가 아니지만 대괄호 안에 있을 경우 메타문자로 기능이 추가된다.  
    ex) [0-9] 0부터 9까지 사이 숫자가 있으면 출력  
    [A-z]는 모든 알파벳이 아니다. 아스키코드로 따지면 대문자와 소문자 사이에 특수문자가 있다.  
    그러므로 [A-Za-z]로 사용해야한다. [A-Z,a-z]가 아닌 이유는 [abcd]를 생각하면 된다. 
    ```python
    print(re.search('[a-z]', s)) # <re.Match object; span=(0, 1), match='h'>
    print(re.search('h[a-z]', s)) # <re.Match object; span=(0, 2), match='he'>
    _s = ']01234'
    print(re.search('[A-z]', _s)) # <re.Match object; span=(0, 1), match=']'>
    # \는 아스키코드 값으로 Z와 a 사이에 있는 아스키코드이다.
    # 즉 A-z라는 것은 A-Z(65-90) + 특정 특수 문자(91-96) + a-z(97-122) 이다.
    ```
    
    - #### ^
    >^는 여는 대괄호([) 뒤에 바로 있으면 ^뒤 문자는 예외처리이다. 즉 여집합
    \[^abcd] a나 b나 c가 아닌 것들 ~(a or b or c)
    ```python
    print(re.search('[^abcd]', s)) # <re.Match object; span=(0, 1), match='h'>
    print(re.search('[^helo]', s)) # <re.Match object; span=(5, 6), match='w'>
    ```


- ### .
>.은 모든 문자와 일치를 나타낸다.  
> 개행문자는 포함하지않는다.
```python
print(re.search('h...o', s)) # <re.Match object; span=(0, 5), match='hello'>
```

## 5. flags
```python
re.search(pattern, string, flags)
```
매개변수 중 flags를 살펴보자

- ### re.I
> 대소문자 구분 없이 일치
```python
s = 'Hello'
print(re.search('he', s)) # None
print(re.search('he', s, re.I)) # <re.Match object; span=(0, 2), match='He'>
```
- ### re.S
> .에 개행문자를 포함한다. 원래는 포함되있지않다.
```python
s = 'Hello\nhello'
print(s)
print(re.search('o..', s)) # None
print(re.search('o..', s, re.S)) # <re.Match object; span=(4, 7), match='o\nh'>
```

- ### inline flag , |
> 여러 종류를 한꺼번에 사용할 수도 있다.
```python
# |사용
print(re.search('h...o..', s, re.S | re.I)) # <re.Match object; span=(0, 7), match='Hello\nh'>
# inline flag로도 할 수 있다.
print(re.search('(?is)h...o..', s)) # <re.Match object; span=(0, 7), match='Hello\nh'>

# 일부로 사용하려면 (?s:pattern)으로 묶어주면 된다.
print(re.search('o..ello', s)) # \n가 포함이안되므로 None
print(re.search('(?is:O..)ello', s)) #<re.Match object; span=(4, 11), match='o\nhello'>
# \와 대소문자 구분 상관 X
```

## 6. 특수 시퀸스
- ### \d 숫자형 \D 비숫자형
```python
s = '543he21'
print(re.search('\d\d', s)) # <re.Match object; span=(0, 2), match='54'>
print(re.search('[0-9][0-9]', s)) # <re.Match object; span=(0, 2), match='54'>
```
- ### \w 단어 \W 비단어
> \w -> 문자형 = 영문+숫자+언더바(_)  
> \W -> \w의 반대
```python
s = '0_D a A'
print(re.search('\w\W\w', s)) # <re.Match object; span=(2, 5), match='D a'>
print(re.search('[0-9A-Za-z_][^0-9A-Za-z_][0-9A-Za-z_]', s)) #<re.Match object; span=(2, 5), match='D a'>
```
- ### \b \B
>\b 단어문자와 비단어문자사이  
즉 a\b -> a뒤에는 비문자가 와야한다.  
!\b -> 느낌표 뒤에는 문자가 와야한다.  
\B  단어문자와 단어문자사이 혹은 비단어문자와 비단어문자사이
```python
s = 'up date up'
print(re.findall(r'\bup\b', s)) # ['up', 'up']
print(re.search(r'\Bat\B', s)) #<re.Match object; span=(4, 6), match='at'>
```
> 처음과 끝은  비문자이다.

```python
s = 'a'
print(re.findall(r'\b', s)) # ['', ''] 처음부분(비문자) + a(문자), a(문자) + 끝부분(비문자) 이래서 2개
print(re.findall(r'\B', s)) # 비문자+비문자, 문자+문자가 없다.

s = 'a aa'
print(re.findall(r'\b', s)) # ['', '', '', '']
# 처음부분(비문자) + a(문자), a(문자) + 끝부분(비문자), 첫번째a(문자)+ 스페이스(비문자), 스페이스(비문자)+ 첫번째a(문자) 총4개
print(re.findall(r'\B', s)) # ['']
# 두번째a(문자) + 세번째a(문자)

s = "!@"
print(re.search(r'\B!', s)) # <re.Match object; span=(0, 1), match='!'>
print(re.search(r'\B!\B', s))# <re.Match object; span=(0, 1), match='!'>
print(re.search(r'@\B', s)) # <re.Match object; span=(1, 2), match='@'>
```


- ### ^,$ 행 \A,\Z 문자열 전체
    - #### \A,\Z 
    > 문자열의 시작과 끝을 나타낸다.
    ```python
    s = 'hello'
    print(re.search('\Ahello\Z', s)) #<re.Match object; span=(0, 5), match='hello'>
    s = 'hello\n'
    print(re.search('\Ahello\Z', s)) #None
    # \n은 문자로 인식이 된다. 
    print(re.search('\Ahello\n\Z', s)) #print(re.search('\Ahello\Z', s)) 
    ```
    - #### ^,$
    > ^와 $는 행의 시작과 행의 끝이다.
    >re.M옵션을 줘야한다.  
    행은 문자열의 시작과 개행문자 사이, 개행문자와 개행문자 사이, 개행문자와 문자열의 끝 사이부분이다.
    ```python
    s = ' hello1 \n hello2 \n hello3 '
    print(re.findall('^\shello\d\s$', s, re.M)) # [' hello1 ', ' hello2 ', ' hello3 ']
    ```
    - #### 빈 문자열 혹은 빈 행 검사
    ```python
    print(re.fullmatch('\A\Z', '')) # <_sre.SRE_Match object; span=(0, 0), match=''>
    print(re.fullmatch('\A\Z', '\n')) # None
    print(re.fullmatch('^$', '')) # <_sre.SRE_Match object; span=(0, 0), match=''>
    print(re.fullmatch('^$', '\n')) # None
    print(re.findall('^$', '\n', re.M)) # ['', '']
    ```
