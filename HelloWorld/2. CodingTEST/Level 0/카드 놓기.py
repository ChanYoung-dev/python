from itertools import permutations

total_card = int(input())
picked_card = int(input())
array_card = [ input() for i in range(total_card)]

class Solution:
    def solution(self):
        permutated_num = set()
        for a in permutations(array_card, picked_card):
            permutated_num.add(''.join(a))
        return (len(permutated_num))


a = Solution()
print(a.solution())
# 순열 조합 응용문제
