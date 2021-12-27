#그리드
n, m = map(int, input().split())
index = 0
count = 0
for _ in range(int(input())):
    pointer = int(input()) - 1
    #print("현재 index:{0}, pointer:{1}, count:{2}".format(index, pointer, count))
    gap = 0
    if pointer < index:
        #print("pointer가 index 왼쪽에 있다")
        gap = index - pointer
        index -= gap
    elif index + m <= pointer:
        #print("pointer가 index 오른쪽에 있다")
        gap = pointer - index - (m - 1)
        index += gap
    count += gap
print(count)