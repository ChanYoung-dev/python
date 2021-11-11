import re
class Solution:
    def solutionA(self, dartResult):
        numbers = re.findall('\d+',dartResult)
        for i,number in enumerate(numbers):
            numbers[i]=int(number)
        multiflies = re.findall('[SDT]',dartResult)
        options = re.split('\d+[SDT]', dartResult)
        del options[0]

        for i, values in enumerate(options):
            if multiflies[i] == 'D':
                numbers[i] = numbers[i] ** 2
            elif multiflies[i] == 'T':
                numbers[i] = numbers[i] ** 3
            if options[i] == '*':
                if (i+1) <= len(options)-1 and options[i+1] == '*':
                    numbers[i] = numbers[i] * 4
                else:
                    numbers[i] = numbers[i] * 2
            elif options[i] == '#':
                if (i+1) <= len(options)-1 and options[i+1] == '*':
                    numbers[i] = numbers[i] * (-2)
                else:
                    numbers[i] = numbers[i] * (-1)
            elif options[i] == '':
                if (i+1) <= len(options)-1 and options[i+1] == '*':
                    numbers[i] = numbers[i] * 2
        return sum(numbers)
a = Solution()
print(a.solutionA("1S2D*3T"))