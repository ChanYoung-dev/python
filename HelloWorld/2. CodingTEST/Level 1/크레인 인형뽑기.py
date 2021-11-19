import collections
class Solution:
    def solutionA(self, board, moves):
        stack = []
        count = 0
        for i in moves:
            for value in board:
                if value[i-1] != 0:
                    if len(stack) > 0 and stack[-1] == value[i-1]:
                        stack.pop()
                        count += 2
                    else:
                        stack.append(value[i-1])
                    value[i-1] = 0
                    break
        return count

a = Solution()
print(a.solutionA([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))