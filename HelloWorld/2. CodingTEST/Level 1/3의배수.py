input_value = input()


class Solution:
    count = 0

    def solution(self):
        def is_single_num(number):
            if sum(number) % 3 != 0:
                return 'NO'
            else:
                return 'YES'

        def go_single_num(number):
            num = list(map(int, list(number)))
            if int(number) < 10:
                return is_single_num(num)
            self.count += 1
            if sum(num) < 10:
                return is_single_num(num)
            else:
                return go_single_num(str(sum(num)))

        answer = str(self.count) + '\n' + go_single_num(input_value)
        return answer


a = Solution()
print(a.solution())
# 재귀함수
# recursive
