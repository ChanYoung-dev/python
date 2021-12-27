#그리드
import collections
_ = input()
heights = list(map(int, input().split()))
result_i = -1
result = -1
count_array = collections.defaultdict(int)
for height in heights:
    if result < height:
        result = height
    else:
        count_array[result] += 1
print(count_array)
counter = collections.Counter(count_array)
print(counter.most_common(1)[0][1])
