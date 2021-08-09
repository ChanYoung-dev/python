num_list=[]
for i in range(0,3):
    A = int(input("{0}번째 숫자를 입력해주세요:".format(i+1)))
    if not A:
        break
    num_list.append(A)
# 방법 1
max = num_list[0] if num_list[0] > num_list[1] else num_list[1]
max = num_list[2] if num_list[2] > max else max

print("max : {0}".format(max))
# 방법 2
[num_list[0], num_list[1]] = [num_list[0], num_list[1]] if num_list[0] > num_list[1] else [num_list[1], num_list[0]]
[num_list[1], num_list[2]] = [num_list[1], num_list[2]] if num_list[1] > num_list[2] else [num_list[2], num_list[1]]

[num_list[0], num_list[1]] = [num_list[0], num_list[1]] if num_list[0] > num_list[1] else [num_list[1], num_list[0]]

print(num_list)