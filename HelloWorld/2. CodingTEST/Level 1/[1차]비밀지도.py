class Solution:
    def solutionA(self, n, arr1, arr2):
        answer = []
        for num1, num2 in zip(arr1, arr2):
            a, b = bin(num1)[2:], bin(num2)[2:]
            while len(a) != n:
                a = '0' + a
            while len(b) != n:
                b = '0' + b
            answer.append(''.join(['#' if (int(a[i]) or int(b[i])) else ' ' for i in range(n)]))
        return answer

a = Solution()
print(a.solutionA(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))