import collections
class Solution:
    def solutionA(self, answers):
        result = []
        count = collections.defaultdict(int)
        a = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

        for i in range(3):
            for index in range(len(answers)):
                if a[i][index % len(a[i])] == answers[index]:
                    count[i + 1] += 1

        most = collections.Counter(count)
        max_value = most.most_common(1)[0][1]
        return [i for i, j in count.items() if max_value == j]

        return result


a = Solution()
print(a.solutionA([1]))