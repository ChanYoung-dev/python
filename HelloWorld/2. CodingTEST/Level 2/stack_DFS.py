def iterative_dfs(graph, start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

class Solution:
    def solutionA(self, num, graphv):
        print(f'recursive dfs: {iterative_dfs(graphv, num)}')

a = Solution()
print(a.solutionA(1, graphv = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3],}))