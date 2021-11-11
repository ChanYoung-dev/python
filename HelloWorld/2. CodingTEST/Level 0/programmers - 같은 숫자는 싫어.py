class Solution:
    def solutionA(self, arr):
        answer = [arr[0]]
        a = arr[0]
        for i in arr:
            if a != i:
                a = i
                answer.append(i)
        return answer

a = Solution()
print(a.solutionA([1, 1, 3, 3, 0, 1, 1]))