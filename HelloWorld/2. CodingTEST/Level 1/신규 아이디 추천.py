import re


def convertToUpper(matchObj):
    up_char = matchObj.group().lower()
    return up_char

class Solution:
    def solutionA(self, new_id):
        deleteChar = ['-','_','.']
        new_id = re.sub('[A-Z]', convertToUpper, new_id)
        new_id = re.sub('[^A-Za-z0-9\-\.\_]', '', new_id)
        print("2단계:", new_id)
        '''
        for i in new_id:
            if i.isalnum() is not True:
                if i not in deleteChar:
                    new_id = new_id.replace(i, '')
        '''
        #print("2단계:", new_id)
        new_id = re.sub('\.+', '.', new_id)
        #print("3단계:", new_id)
        new_id = re.sub('\A\.|\.\Z', '', new_id)
        #print("4단계:", new_id)
        if new_id == '':
            new_id += 'a'
        #print("5단계:", new_id)
        new_id = re.sub('(?<=.{15}).*', '', new_id)
        new_id = re.sub('\.\Z', '', new_id)
        #print("6단계:", new_id)
        while len(new_id) <= 2:
            new_id += new_id[-1]
            #new_id = re.sub('.(?=\Z)', '\g<0>\g<0>', new_id)

        #print("7단계:", new_id)
        #print("최종",new_id)
        return new_id

a = Solution()
print(a.solutionA("z."))