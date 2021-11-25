def recursive_dfs(graph, v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(graph, w, discovered)
    return discovered

class Solution:
    def solutionA(self, num, graphv):
        print(f'recursive dfs: {recursive_dfs(graphv, num)}')

a = Solution()
print(a.solutionA(1, graphv = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3],}))