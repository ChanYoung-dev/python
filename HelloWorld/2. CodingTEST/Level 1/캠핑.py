class Solution:
    def solution(self):
        array = []
        while True:
            a = input().split()
            if a == ['0', '0', '0']:
                break
            array.append(list(map(int, a)))

        for i, test in enumerate(array):
            result = 0
            result += test[0]*(test[2]//test[1])
            if test[2] % test[1] <= test[0]:
                result += (test[2] % test[1])
            else:
                result += test[0]
            print("Case {0}: {1}".format(i+1, result))
        quit()

a=Solution()
print(a.solution())
#그리드