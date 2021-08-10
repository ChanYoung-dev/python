a = 10
b = 10
c = 11
print(a, 'id =', id(a)) # 4365484080
print(b, 'id =', id(b)) # 4365484080
print(c, 'id =', id(c)) # 4365484112
print('같은 객체' if a is b else '다른 객체') # 같은 객체
print('같은 객체' if a is c else '다른 객체') # 다른 객체
c=10
print('같은 객체' if a is c else '다른 객체') # 같은 객체