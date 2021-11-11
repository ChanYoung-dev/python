class Solution:
    def solutionA(self, numbers):
        answer=[]
        numbers.sort()
        #print(numbers)
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                #print(numbers[i], numbers[j])
                if numbers[i]+numbers[j] not in answer:
                    answer.append(numbers[i]+numbers[j])
        return answer



a = Solution()
print(a.solutionA([2,1,3,4,1]))