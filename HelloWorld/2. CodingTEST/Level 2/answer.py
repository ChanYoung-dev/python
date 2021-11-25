class Solution:
    def solution(self, n, s, num_rooms):
        def func(i, j, vertical):
            num_list = [num_rooms[i][j]] if vertical else [num_rooms[j][i]]
            for index in range(i + 1, n):
                num_list += [num_rooms[index][j]] if vertical else [num_rooms[j][index]]
                array = num_list + [num_rooms[index][j_index] if vertical else num_rooms[j_index][index] for j_index in range(j + 1, n)]
                while sum(array) > s:
                    array.pop()
                if sum(array) == s:
                    answer.append(array)
        answer = []
        for k in range(n):
            for l in range(n):
                func(k, l, vertical=True)
                func(l, k, vertical=False)
        return answer
a=Solution()
print(a.solution(4, 11, num_rooms=[[2, 4, 2, 6], [6, 6, 4, 2], [2, 2, 1, 2], [4, 4, 5, 3]]))