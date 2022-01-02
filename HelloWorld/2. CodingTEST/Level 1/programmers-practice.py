from itertools import permutations

x = input()



class Solution:
    count = 0
    def solution(self, i):

        def go_single_num(number):
            num = list(map(int, list(number)))
            if int(number) < 10:
                return 0
            print(type(x), x)

            print(sum(num))
            self.count += 1
            print("count", self.count)
            if sum(num) < 10:
                return 0
            else:
                return go_single_num(str(sum(num)))

        answer = go_single_num(x)
        return answer


a = Solution()
print(a.solution(x))
# 그리드
# 수학문제
