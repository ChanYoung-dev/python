class Solution:
    def solutionA(self, dirs):
        current = [0, 0]
        check = set()
        check.add(tuple((4,3,4,2)))
        print(check)
        for dir in dirs:
            if dir == 'U' and current[1] != 5:
                past = str(current)
                current[1] += 1
                if (str(current)+past) in check:
                    continue
                check.add(past + str(current))
            elif dir == 'D' and current[1] != -5:
                past = str(current)
                current[1] -= 1
                if (str(current)+past) in check:
                    continue
                check.add(past + str(current))
            elif dir == 'R' and current[0] != 5:
                past = str(current)
                current[0] += 1
                if (str(current)+past) in check:
                    continue
                check.add(past + str(current))
            elif dir == 'L' and current[0] != -5:
                past = str(current)
                current[0] -= 1
                if (str(current)+past) in check:
                    continue
                check.add(past + str(current))
        #print(check)
        return len(check)

a = Solution()
print(a.solutionA("LLLLLLLLULLLLDDU"))