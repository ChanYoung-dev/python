class Solution:
    def solutionA(self, arr1, arr2):
        answer = []
        for n in range(len(arr1)):
            answer.append([(arr1[n][index] + arr2[n][index]) for index in range(len(arr1[0]))])
        return answer

a = Solution()
print(a.solutionA([[1, 2], [2, 3]], [[3, 4], [5, 6]]))