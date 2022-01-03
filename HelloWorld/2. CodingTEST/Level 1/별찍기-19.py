


class Solution:
    space = -1
    def solution(self):

        number_repetitions = int(input())
        pattern = ['*']

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
# 재귀
