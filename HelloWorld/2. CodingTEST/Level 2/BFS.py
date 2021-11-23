def iterative_bfs(graph, start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

class Solution:
    def solutionA(self, num, graphv):
        print(f'recursive dfs: {iterative_bfs(graphv, num)}')

a = Solution()
print(a.solutionA(1, graphv = {1: [2, 3, 4], 2: [5], 3: [5], 4: [], 5: [6, 7], 6: [], 7: [3],}))