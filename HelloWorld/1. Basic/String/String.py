# 슬라이싱
s = 'hellow'
print(s[1:4]) #ell / index1부터 4-1 까지 출력
print(s[1:-2]) #ell / index1부터 뒤에서2번째이전까지 출력 / 뒤에서 1번째가 인덱스 -1이다.
print(s[:]) # hellow /복사가 된다. 이때 참조가 아닌 값 복사이다. list같은경우에 유용하다. 왜냐하면 list는 가변객체이기때문에 참조하기 때문이다.
print(s[1]) # e
print(s[::-1]) #wolleh
print(s[::2]) #hlo

# 정규표현식(re)
# 특정 문자를 찾거나 찾은 문자를 다른 문자로 대체해주는 등 문자열 조작방법 중 하나
# 메타문자
# ` $()*+.?[\^{
# 기능을 갖은 문자이다. 이 문자를 찾고 싶으면 백슬래시(\)를 붙여주자 아니면 대괄호 안에 넣어도 된다.
# re를 사용해주기 위해 import를 해주자
import re

# re의 함수
# re.match
# 문자열의 "처음"부터 시작하여 패턴을 찾는다.
s = 'hellow'
print(re.match('h', s)) # <re.Match object; span=(0, 1), match='h'>
print(re.match('e', s)) # None
# h가 처음부터 있으므로 span=(0,1)을 통해 h의 위치인 0부터 1이전(즉,0)을 확인할수 있다.
# e는 hellow안에 있지만 처음부터 없으므로 X

# re.search
# 특정패턴문자가 문자열안에 있는지
print(re.search('h', s)) # <re.Match object; span=(0, 1), match='h'>
print(re.search('e', s)) # <re.Match object; span=(1, 2), match='e'>

# re.findall
# 패턴과 일치하는 모든 부분을 찾아낸다.
print(re.findall('h', s)) # ['h']
print(re.findall('l', s)) # ['l', 'l']
print(re.findall('z', s)) # []
_s = 'hhhh'
print(re.findall('hhh', _s)) # ['hhh']
# 'hhhh' 에서 index0~2인 hhh와 index1~3인 hhh가 있지만 overlapping을 하지않는다.

# re.finditer
# findall과 비슷하지만 Iterator형식으로 패턴 찾은 것을 보여준다.
finditer_obj = re.finditer('h', s)
print("finditer:{}".format(finditer_obj))
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

# re.fullmatch
# 완벽하게 같은 문자열패턴을 찾아준다.
print(re.fullmatch('h', s)) # None
print(re.fullmatch('hell', s)) # None
print(re.fullmatch('hellow', s)) # <re.Match object; span=(0, 6), match='hellow'>

# match_object의 method
# group(), start(), end(), span()
match_Object = re.search('l', s)
print(match_Object) # <re.Match object; span=(2, 3), match='l'>
print(match_Object.group()) # l 일치한 문자열패턴 반환
print(match_Object.start()) # 2 일치한 문자열 시작위치
print(match_Object.end()) # 3 일치한 문자열 끝 위치
print(match_Object.span()) # (2, 3) 일치한 문자열의 시작,끝 튜플로 반환


# 정규식 자료
# 대괄호
# [abcd ] == [ a or b or c or d ]
print(re.search('[zh]', s)) # <re.Match object; span=(0, 1), match='h'>
# z나 h가 들어가면 출력  -> h가 들어갔으므로 출력
print(re.search('he[zl]', s)) # <re.Match object; span=(0, 3), match='hel'>
# hez 나 hel 일 경우 출력

# -는 메타문자가 아니지만 대괄호 안에 있을 경우 메타문자로 기능이 추가된다.
# ex) [0-9] 0부터 9까지 사이 숫자가 있으면 출력
# [A-z]는 모든 알파벳이 아니다. 아스키코드로 따지면 대문자와 소문자 사이에 특수문자가 있다.
# 그러므로 [A-Za-z]로 사용해야한다. [A-Z,a-z]가 아닌 이유는 [abcd]를 생각하면 된다.
print(re.search('[a-z]', s)) # <re.Match object; span=(0, 1), match='h'>
print(re.search('h[a-z]', s)) # <re.Match object; span=(0, 2), match='he'>
_s = ']01234'
print(re.search('[A-z]', _s)) # <re.Match object; span=(0, 1), match=']'>
# \는 아스키코드 값으로 Z와 a 사이에 있는 아스키코드이다.
# 즉 A-z라는 것은 A-Z(65-90) + 특정 특수 문자(91-96) + a-z(97-122) 이다.

# ^는 여는 대괄호([) 뒤에 바로 있으면 ^뒤 문자는 예외처리이다. 즉 여집합
# [^abcd] a나 b나 c가 아닌 것들 ~(a or b or c)
print(re.search('[^abcd]', s)) # <re.Match object; span=(0, 1), match='h'>
print(re.search('[^helo]', s)) # <re.Match object; span=(5, 6), match='w'>



# .은 모든 문자와 일치를 나타낸다.
print(re.search('h...o', s)) # <re.Match object; span=(0, 5), match='hello'>

# flags
# re.search(pattern, string, flags)
# flags를 살펴보자

# re.I
# 대소문자 구분 없이 일치
s = 'Hello'
print(re.search('he', s)) # None
print(re.search('he', s, re.I)) # <re.Match object; span=(0, 2), match='He'>

# re.S
# .에 개행문자를 포함한다. 원래는 포함되있지않다.
s = 'Hello\nhello'
print(s)
print(re.search('o..', s)) # None
print(re.search('o..', s, re.S)) # <re.Match object; span=(4, 7), match='o\nh'>


# 여러 종류를 한꺼번에 사용할 수도 있다.
# |사용
print(re.search('h...o..', s, re.S | re.I)) # <re.Match object; span=(0, 7), match='Hello\nh'>
# inline flag로도 할 수 있다.
print(re.search('(?is)h...o..', s)) # <re.Match object; span=(0, 7), match='Hello\nh'>

# 일부로 사용하려면 (?s:pattern)으로 묶어주면 된다.
print(re.search('o..ello', s)) # \n가 포함이안되므로 None
print(re.search('(?is:O..)ello', s)) #<re.Match object; span=(4, 11), match='o\nhello'>
# \와 대소문자 구분 상관 X

# \d 숫자형 \D 비숫자형
s = '543he21'
print(re.search('\d\d', s)) # <re.Match object; span=(0, 2), match='54'>
print(re.search('[0-9][0-9]', s)) # <re.Match object; span=(0, 2), match='54'>

# \w 단어 \W 비단어
# \w -> 영문+숫자+언더바(_)
s = '0_D a A'
print(re.search('\w\W\w', s)) # <re.Match object; span=(2, 5), match='D a'>
print(re.search('[0-9A-Za-z_][^0-9A-Za-z_][0-9A-Za-z_]', s)) #<re.Match object; span=(2, 5), match='D a'>

# \b \B
# \b 단어문자와 비단어문자사이
# 즉 a\b -> a뒤에는 비문자가 와야한다.
# !\b -> 느낌표 뒤에는 문자가 와야한다.

# \B  단어문자와 단어문자사이 혹은 비단어문자와 비단어문자사이
s = 'up date up'
print(re.findall(r'\bup\b', s)) # ['up', 'up']
print(re.search(r'\Bat\B', s)) #<re.Match object; span=(4, 6), match='at'>

# 처음과 끝은  비문자이다.
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

# ^,$ 행 \A,\Z 문자열 전체
# \A,\Z 문자열의 시작과 끝을 나타낸다.
s = 'hello'
print(re.search('\Ahello\Z', s)) #<re.Match object; span=(0, 5), match='hello'>
s = 'hello\n'
print(re.search('\Ahello\Z', s)) #None
# \n은 문자로 인식이 다.
print(re.search('\Ahello\n\Z', s)) #print(re.search('\Ahello\Z', s)) 된

#^와 $는 행의 시작과 행의 끝이다.
# re.M옵션을 줘야한다.
# 행은 문자열의 시작과 개행문자 사이, 개행문자와 개행문자 사이, 개행문자와 문자열의 끝 사이부분이다.
s = ' hello1 \n hello2 \n hello3 '
print(re.findall('^\shello\d\s$', s, re.M)) # [' hello1 ', ' hello2 ', ' hello3 ']

#빈자열 혹은 빈 행 검사
print(re.fullmatch('\A\Z', '')) # <_sre.SRE_Match object; span=(0, 0), match=''>
print(re.fullmatch('\A\Z', '\n')) # None
print(re.fullmatch('^$', '')) # <_sre.SRE_Match object; span=(0, 0), match=''>
print(re.fullmatch('^$', '\n')) # None
print(re.findall('^$', '\n', re.M)) # ['', '']


# 정규표현식의 기초
# | : 양자택일

s = 'one onetwo'
print(re.findall('one|onetwo', s)) # ['one', 'one']
#onetwo는 나오지 않는다. 그 이유는 첫번째 one에서 첫'one'을 추출하고 두번째 onetwo에서 'one'을 추출하면 two만 검사할패턴이 남았기때문이다.

#이를 해결하기 위해선
print(re.findall('onetwo|one', s)) #['one', 'onetwo']
#긴패턴을 앞에 놓거나
print(re.findall(r'\bone\b|\bonetwo\b', s))  # ['one', 'onetwo']
# \b를 사용하면 된다.

# 정량자
# *, +
# *
# 0회이상 반복
s = 'llhello'
print(re.search('l*', s))
print(re.findall('l*', s)) # ['ll', '', '', 'll', '', '']
# index[0] -> 첫번째 ll에서 한번
# index[1] -> h 앞
# index[2] -> e 앞
# index[3] -> 두번째 ll 앞
# index[4] -> o 앞
# index[5] -> 끝문자열 앞

s = 'hello'
print(re.search('l*', s))#<re.Match object; span=(0, 0), match=''>
#이처럼 0회이상 반복이기때문에 비어있는 것도 포함이다.

# +
#1회이상반복
s = 'llhello'
print(re.findall('l+', s)) #['ll', 'll']
# 1회이상 반복이기때문에 성공적으로 뜨는 것을 확인할 수 있다.
s = '<p> Lorem ipsum... is boring. </p>'
print(re.search('<p>.+</p>', s))
# <re.Match object; span=(0, 34), match='<p> Lorem ipsum... is boring. </p>'>

# {n, m}
'''
a{n} : n회만큼 반복
a{n, m} : n회이상 m회이하 반복
a{n,} : n회이상 반복
'''
# ex{2,5} aabbbaaaaaa -> 첫번째 aa에서 2번이므로 반환하고 두번째 aaaaaa중 aa를 확인하고 반환하는것이아니라
# 어디까지 a가 반복되는지 확인하고 반복횟수 최대 Max를 5까지만 제한을 둔다.
# 단, {,}에서 띄어쓰기를 하면 안된다.
s = 'aabbbaaaaaa'
print(re.findall('a{2, 5}', s)) # [] / 아무것도 안뜬다.
print(re.findall('a{2,5}', s)) # ['aa', 'aaaaa']

# 나태정량자
# 다음 코드를 보자

matchObj = re.search('<p>.*</p>', '''
<p> part 1 </p> part 2 </p>
<p> part 3 </p> part 4 </p>
''', re.DOTALL)
print(matchObj.group())
'''
<p> part 1 </p> part 2 </p>
<p> part 3 </p> part 4 </p>
'''
# 여기서 확인해볼수 있는 것은 .이 </p>도 문자로 인식했다는 것이다.
# 이것을 탐욕 정량자라고 한다. 역행이라고도 표현한다. 끝까지 간다음 맞는 것을 확인하기때문.

matchObj = re.search('<p>.*?</p>', '''
<p> part 1 </p> part 2 </p>
<p> part 3 </p> part 4 </p>
''', re.DOTALL)
print(matchObj.group())
'''
<p> part 1 </p>
'''
#?을 붙이면 나태 정량자라고 한다.

#응용
# 1~8자리 10찐수에 일치하는 정규표현식
# r'\b\d{1,8}\b'

#4자리 또는 8자리 16진수에 일치하는 정규표현식
# r'\b[0-9a-f]{4}\b|\b[0-9a-f]{8}\b'

# ( )
# 그룹화와 캡처
s = 'ab abab baba abbb'
print(re.findall('ab+', s)) # ['ab', 'ab', 'ab', 'ab', 'abbb']
#abab로 인식을 하지않고 a따로 b따로 이기때문에 ab나 abbb, abbbbb같이 b에만 +가 적용된다.

# 이럴땐 묶어주는 소괄호의 기능을 사용하면 된다.
s = 'abab'
print(re.search('(ab)+', s)) # <re.Match object; span=(0, 4), match='abab'>
print(re.findall('(ab)+', s)) #['ab']
#하지만 findall에선 abab가 아니라 ab가 뜨는 것을 확인할 수 있다. 이유는?
# 바로 괄호가 그룹화 기능을 하는 것이 아니라 캡처의 역할을 기능해서 일어난 일
print(re.findall('(?:ab)+', s)) # ['abab']
# 위와 같이 (?:<패턴>) 을 사용해주면 된다.


# 캡처
# 캡처는 원하는 부분만을 추출해준다.
s = '2018:10:20'
print(re.findall('\d{4}:(\d\d):(\d\d)', s)) # [('10', '20')]
# 원하는 부분을 ( )소괄호 해주면 추출된다.

# groups()
# 위는 findall이었다. re.search를 해보자
print(re.search('\d{4}:(\d\d):(\d\d)', s)) # <re.Match object; span=(0, 10), match='2018:10:20'>
# 추출된 것이아니라 검색한 패턴자체가 뜬다.

# 위에서 확인해본 match_object의 method부분에서 group을 사용해보자.
match_Object = (re.search('\d{4}:(\d\d):(\d\d)', s))
print(match_Object.group()) # 2018:10:20
# 마찬가지로 검색한 내용이 뜨는 것을 확인할 수 있다.

for i in range(0, 2+1):
    print("group({0}):{1}".format(i, match_Object.group(i)))
'''
group(0):2018:10:20
group(1):10
group(2):20
'''
# group(0)은 검색한패턴이 똑같이 뜨는 것을 확인할수있고, group(1)과 (2)는 캡처한 목록이 뜬다.

print(match_Object.groups()) # ('10', '20')
print(match_Object.groups()[0]) # 10
print(match_Object.groups()[1]) # 20
#groups 리스트 형식으로 출력해준다.




# 난이도 상 어렵다이제
# \숫자
# \1 은 첫번째 캡처한 그룹, \2 두번째 참조한 그룹
# 소괄호 ( ) 앞에 r을 붙여줘야한다.

# 앞뒤가 똑같은 문자열 찾기
print(re.search(r'(\w)\w\1', '기러기 ABC aba xyxy ').group()) #기러기
# 첫번째 캡처한 것은 맨처음(\w)이다.
# 기러기 로 치면 '기'러기에서 앞 '기'를 캡처한 것이고
# \1자리에 첫번째 캡처한 문자인 '기'와 같은 패턴을 추출한다.
# 하지만 search이기때문에 처음 한번 검사를 하고 만다.
print(re.search(r'(\w)\w\1', '기러기 ABC aba xyxy ').group(1))
print(re.search(r'(\w)\w\1', '기러기 ABC aba xyxy ').groups())
print(re.findall(r'(\w)\w\1', '기러기 ABC aba xyxy ')) # ['기', 'a', 'x']
#여러번 검사하여 앞뒤가 같은 문자인 기러기와 aba와 aba를 패턴을 찾지만 캡처만 반환하므로 (\w)부분만 반환한다.

# 이럴 땐, 캡처를 하나 더 만들면 된다.
match_List = re.findall(r'((\w)\w\2)', '기러기 ABC aba xyxy ')
print(match_List) # [('기러기', '기'), ('aba', 'a'), ('xyx', 'x')]
# 캡처의 우선순위가 바깥괄호가 우선이기때문에 첫번째 인자로 '기러기'가 나타나고 두번째 인자로 두번째캡처인 '기'가 나타난다.
for match in match_List:
    print(match[0],end=' ')
#기러기 aba xyx

match_Object_Iter = re.finditer(r'((\w)\w\2)', '기러기 ABC aba xyxy ')
print(match_Object_Iter)
for match in match_Object_Iter:
    print('찾은 패턴: {}, 캡처한 패턴: {}, 첫번째 캡처: {}, 두번째 캡처:{} start/end position={}'.
          format(match.group(), match.groups(), match.group(1), match.group(2), match.span()))
'''
찾은 패턴: 기러기, 캡처한 패턴: ('기러기', '기'), 첫번째 캡처: 기러기, 두번째 캡처:토 start/end position=(0, 3)
찾은 패턴: aba, 캡처한 패턴: ('aba', 'a'), 첫번째 캡처: aba, 두번째 캡처:a start/end position=(8, 11)
찾은 패턴: xyx, 캡처한 패턴: ('xyx', 'x'), 첫번째 캡처: xyx, 두번째 캡처:x start/end position=(12, 15)
'''
# finditer는 iterator 형식으로 반환하기때문에 re.search를 반복해서 iterate해준다.

print(re.findall(r'\b(\d\d)+\b', '1, 25, 301, 4000, 55555')) # ['25', '00']
# 길이가 짝수인 숫자를 찾고 싶다.
# 하지만 결과 값은? 4000이 아니라 00이 뜬다.
#해결방법1.
print(re.findall(r'\b(?:\d\d)+\b', '1, 25, 301, 4000, 55555')) #['25', '4000']

# 해결방법2.
print(re.search(r'\b(\d\d)+\b', '1, 4000, 301, 25, 55555')) # <re.Match object; span=(3, 7), match='4000'>
# search 처음 발견한 것만 뜬다.
# 이를 이용하여

matchObj_iter = re.finditer(r'\b(\d\d)+\b', '1, 25, 301, 4000, 55555')

for matchObj in matchObj_iter:
    print(matchObj.group())
'''
25
4000
'''
# re.search를 반환하는 re.finditer를 이용하여 출력해준다.

# \1 \2 대신 (?P<name>pattern)을 사용하여 직관적으로 볼수있다.
print(re.search(r'(?P<name>\w{3}) (?P=name)\w', '기러기 기러기기 aba xyxy '))#<re.Match object; span=(0, 8), match='기러기 기러기기'>
# 찾는 패턴 (\w\w\w) (\w\w\w)\w 첫번째(\w\w\w)와 두번째(\w\w\w)는 같아야한다.
print(re.search(r'(?P<name>\w{3}) (?P=name)\w', '기러기 기러기기 aba xyxy ').groups()) #('기러기',)
# 캡처항목 : (?p<name>) 부분

#치환
# re.sub(pattern, repl, string, count, flags)
# 치환1
# 지정한 문자로 치환하기
password = 'abcdefg abcdefg abcdefg'
print(re.sub('d\w{3}', 'XXXX', password)) # abcXXXX abcXXXX abcXXXX

#count는 치환할 숫자이다.
print(re.sub('d\w{3}', 'XXXX', password, 2)) # abcXXXX abcXXXX abcdefg

#치환을 이용하여 일부문자열 제거
print(re.sub('d\w{3}', '', password, 2)) # abc abc abcdefg

# 치환2
# 치환으로 문장속 문장과 일치하는 내용 넣기
print(re.sub('김찬영', '[범인]:\g<0>', '김찬영은 범인이고 강민숙은 범인의 여자친구이다.'))
# 김찬영은 범인이고 ~ -> [범인]김찬영은 범인이고~
print(re.sub('(김찬영)은 범인이고 (강민숙)은 범인의 여자친구이다.', r'\1:범인 \2:여자친구', '김찬영은 범인이고 강민숙은 범인의 여자친구이다.'))
# 김찬영:범인 강민숙:여자친구
# \1,\2를 넣을땐 r을 소괄호앞에 넣어주자.
print(re.sub('(?P<suspect>\w{3})은 범인이고 (?P<girlfriend>\w{3})은 범인의 여자친구이다.',
             '\g<suspect>:범인 \g<girlfriend>:여자친구',
             '김찬영은 범인이고 강민숙은 범인의 여자친구이다.'))
#김찬영:범인 강민숙:여자친구

# re.split(pattern, string, maxsplit, flags)
result = re.split(':', ':1992:03:05:')
print(result)
result = re.split('<[^<>]*>',
                  '<html> Wow <head> header </head> <body> Hey </body> </html>')
print(result)
#['', ' Wow ', ' header ', ' ', ' Hey ', ' ', '']


# 치환3
# 함수화한 문장을 치환해서 넣기
def convertToPercentage(matchObj):
    number = float(matchObj.group())
    return str(number * 100) + '%'

print(re.sub(pattern=r'\b0\.\d+\b',
             repl=convertToPercentage,
             string='Red 0.250, Green 0.001, Blue 0.749, Black 1.5'))
# Red 25.0%, Green 0.1%, Blue 74.9%, Black 1.5
# 여기서 matchObj는 re.finditor값인 것을 알 수 있다.

#행나누기 방법
string = '''java - Click on button until alert is present in Selenium	2017년 5월 23일
Click OK on alert Selenium Webdriver	2016년 6월 5일
python - Click the javascript popup through webdriver	2012년 5월 29일
selenium - Read Message From Alert and click on OK	2012년 5월 17일
stackoverflow.com 검색결과 더보기'''
lines = re.split('\r?\n', string)
print(lines[0])
# 윈도우는 \r\n 리눅스는 \n이기때문
print(re.findall('.+', string)[0])
# .은 개행문자가 포함이 안되므로 개행문자 전까지 찾는다.
print(re.findall('^.+$', string, re.M)[0])
# ^와 $는 re.M의 flags와 같이 사용할시 개행문자의 의미를 갖는다.

# 전방탐색과 후방탐색
# 긍정 전방탐색 (?=<pattern>)
# 긍정 후방탐색 (?<=<pattern>)
# 부정 전방탐색 (?!<pattern>)
# 부정 후방탐색 (?<!pattern>)
s = 'name김찬영'
a = 'name'
print(re.search('(?<=name)\w+(?=\Z)', s)) #<re.Match object; span=(4, 7), match='김찬영'>
# (\w+) 앞에 name이 있고 (\w+)뒤에 \Z가 있으면(끝이 나면) name을 출력


password = 'abcdefg'
print(re.sub('(?<=\w{3})\w+(?=\Z)','***' ,password))
#앞자리 3개 말고는 다 가리기
password = 'abcdefgggggggg'
print(re.sub('\w{3}(?=\Z)','XXX' ,password))
# 뒷자리 3개만 가리기

# 정규식 안에 변수 넣기
# '+변수+'
a = str(len(password)//2)
print("a:", type(a))
print(re.sub('\w{'+a+'}(?=\Z)','X'*int(a) ,password))
# 변수는 str형만 가능하다.
a ='abc'
print(re.sub(a+'d', 'X' ,password))

a = 'name'
print(re.search('(?<=name)\w+(?=\Z)', s)) #<re.Match object; span=(4, 7), match='김찬영'>
#이 식은 다음과 같이 사용할 수도 있다.
print(re.search(f'(?<={a})\w+(?=\Z)', s)) #<re.Match object; span=(4, 7), match='김찬영'>
# 괄호앞에 f를 넣어준다. 그리고 변수를 {}로 감싸준다.


print(re.findall(r'[a-z]+\d+(?!!)\b', 'tube1109! gorio303 ryan416'))
# 끝자리에 !가 없는 것 추출

# compile과 퀴즈 풀어보기




