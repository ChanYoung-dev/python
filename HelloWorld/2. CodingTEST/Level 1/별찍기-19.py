import collections


class Solution:
    space = -1
    def solution(self):
        number_repetitions = int(input())
        pattern = collections.deque()
        pattern.append('*')
        def recursive():
            if number_repetitions * 4 - 5 == self.space:
                return '\n'.join(list(pattern))
            self.space += 4
            for key, value in enumerate(pattern):
                pattern[key] = '* ' + value + ' *'
            added_pattern = ['*' + ' ' * self.space + '*', '*' + '*' * self.space + '*']
            pattern.extendleft(added_pattern)
            pattern.extend(added_pattern)


            return recursive()
        return recursive()


a = Solution()
print(a.solution())
# 재귀
# deque
