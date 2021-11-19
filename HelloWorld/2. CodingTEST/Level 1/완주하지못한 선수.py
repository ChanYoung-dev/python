import collections
class Solution:
    def solutionA(self, participant, completion):
        answer = collections.Counter(participant) - collections.Counter(completion)
        print(list(answer.keys())[0])
        '''
        내가 푼 방법 
        dict는 추출이나 제거가 O(1)이다.
        completion_dict = collections.defaultdict(int)
        for i in completion:
            completion_dict[i] += 1

        for check in participant:
            if check not in completion_dict or completion_dict[check] == 0:
                return check
            completion_dict[check] -= 1
        '''


a = Solution()
print(a.solutionA(["mislav", "mislav", "mislav", "ss"], ["mislav", "mislav", "mislav"]))