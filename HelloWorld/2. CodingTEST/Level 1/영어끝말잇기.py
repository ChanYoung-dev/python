import re
class Solution:
    def solutionA(self, n, words):
        past_word = { words[0]:0 }
        for i in range(1, len(words)):
            if words[i][0] != words[i-1][-1] or words[i] in past_word:
                return [(i//n)+1, (i%n)+1]
            else:
                past_word[words[i]] = 1
        return [0, 0]
a = Solution()
print(a.solutionA(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))