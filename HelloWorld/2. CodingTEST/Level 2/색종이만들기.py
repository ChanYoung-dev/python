repetition = int(input())
arrays = [list(map(int, input().split(' '))) for _ in range(repetition)]

class Solution:
    def solution(self):
        def func(checks):
            num_lists = [[], [], [], []]
            check_num = 1 if checks[0][0] == 0 else 0
            for check in checks:
                if check_num in check:
                    break
            else:
                if check_num == 1:
                    result.append(0)
                else:
                    result.append(1)
                return str(result.count(0)) + '\n' + str(result.count(1))
            for i, check in enumerate(checks):
                if i < len(checks)/2:
                    num_lists[0].append(check[:int(len(checks)/2)])
                    num_lists[1].append(check[int(len(checks)/2):])
                else:
                    num_lists[2].append(check[:int(len(checks)/2)])
                    num_lists[3].append(check[int(len(checks)/2):])
            for num_list in num_lists:
                func(num_list)
            return str(result.count(0)) + '\n' + str(result.count(1))
        result = []
        return func(arrays)

a = Solution()
print(a.solution())
# 재귀
