


#첫번째 방법
# 0x 0 6 6 0 은 0b 0000 0110 0110 0000 이다
# mark는        0b 1000 0000 0000 0000 이다
# and연산자를 하면 0b 0000 0000 0000 0000 이다.
# >> 연산자를 통해 자리수마다 계속 확인한다
# 예를 들어 >>5이면
# 0b 0000 0110 0110 0000
# 0b 0000 0100 0000 0000
#=0b 0000 0100 0000 0000
# 즉 (i & mark) == mark이기때문에 ■를 넣을수 있다.
brick = (0x0660, 0x0F00, 0x2222, 0x6220, 0x4460, 0x4640, 0x7200, 0x6300,0x4620)

for i in brick:
    mark = 0b1000000000000000
    for j in range(0,16):
        print('■',end=' ') if (i & mark) == mark else print('ㅁ', end=' ')
        if not (j+1)%4:
            print()
        mark >>= 1

#직접 비교이다
# mark = i 로 하면 십진수로 표현이 되기때문에
# bin(i)를 통해 0b11001100000
# str(bin(i)) 자르기를 위해 문자열로 변환 0b11001100000
# 0b를 지우기위해 str(bin(i))[2:] 11001100000
# 앞부분을 0으로 채우기위해 0000011001100000

#두번째 방법
brick = (0x0660, 0x0F00, 0x2222, 0x6220, 0x4460, 0x4640, 0x7200, 0x6300,0x4620)
for i in brick:
    mark = str(bin(i))[2:].zfill(16)
    print(mark)
    for j in range(0, 16):
        print('■', end= '') if (mark[j] == '1') else print('ㅁ', end= '')
        if not ((j+1)%4):
            print()


