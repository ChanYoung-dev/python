def func(x):
    return -1*int(x)


def solution(n):
    result = list(str(n))
    result = sorted(result, key = func)
    result = ''.join(result)
    return int(result)