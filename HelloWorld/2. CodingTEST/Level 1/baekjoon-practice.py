


class Solution:
    def solution(self):
        space = -1
        number_repetitions = int(input())
        pattern = ['*']

        def recursive():
            if number_repetitions * 4 - 5 == space:
                return '\n'.join(pattern)

        return recursive()


        def recursive():
            if number_repetitions * 4 - 5 == self.space:
                return '\n'.join(pattern)
            self.space += 4
            for key, value in enumerate(pattern):
                pattern[key] = '* ' + value + ' *'
            first = '*' + ' ' * self.space + '*'
            second = '*' + '*' * self.space + '*'
            pattern.insert(0, first)
            pattern.insert(0, second)
            pattern.append(first)
            pattern.append(second)
            return recursive()

        return recursive()

a = Solution()
print(a.solution())
# 순열 조합 응용문제
