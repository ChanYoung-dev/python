list_comprehension = [ n * 2 for n in range(1, 10+1) if not n%2]
print(list_comprehension)
# [4, 8, 12, 16, 20]

list_comprehension = []
for n in range(1, 10+1):
    if n % 2 == 0:
        list_comprehension.append(n*2)

print(list_comprehension)
# [4, 8, 12, 16, 20]

original = {"나": "김찬영", "친구": "강민숙"}

dict_comprehension = {}
for key, value in original.items():
    dict_comprehension[key] = value
print(original)
print(dict_comprehension)

dict_comprehension = {key: value for key, value in original.items()}
print(dict_comprehension)

a = [n for n in range(100)]
b = range(0, 100+1, 2)
print(a[99])
print(b[50])



def test():
    c = 5
    d = 4
    print(locals())

test()
print(locals())
