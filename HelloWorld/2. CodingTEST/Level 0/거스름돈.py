#그리드
data = input()

answer = 1000 - int(data)
array = [500, 100, 50, 10, 5, 1]
result = 0
for i in array:
    result += answer // i
    answer -= ((answer // i) * i)
print(result)