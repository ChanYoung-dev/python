# 가장 긴 팰린드롬 부분 문자열
# https://leetcode.com/problems/longest-palindromic-substring/
# page.159

# 신경써야할 것 :
# 1. 처음부터 문자열을 뒤집어봐서 전체문자열이 이미 팰린드롬인지를 확인해본다.
# 위과정을 안하면 전체문자열이 팰린드롬일때 쓸데없는 검사를 많이 진행해야만 판단할수 있기때문에 Time Limit Exceeded오류가 뜬다.
# ex) 'bbbbbbbbbbbbbbbb~~~bbbbbbbbb'
# 2. 단어 하나만 있는 것은 어차피 팰린드롬이다.
# 3. 해당하는 단어가 없을시 default처리로 맨앞 첫번째 원소로 정해준다.

# 풀이
# 홀수개씩 확장해가며 검사와 짝수개씩 확장해가며 검사 두가지를 진행한다.
# 예시)홀수개
# cbabad를 예시로 들면 s[0]부터 s[2]까지의 문자열을 뒤집어도 같은 지 확인
# 다를시 한칸더앞으로 체크 s[1]부터 s[3] 까지의 문자열을 뒤집어도 같은 지 확인
# 같으니까 j를 한칸씩 확장시키며 검사
# s[1-j]부터 s[3+j]의 문자열을 검사하며 틀릴때까지 검사한다.
# 팰린드롬인지 확인되는 문자열들은 전부 str_list 문자열에 넣어준다.
# max를 통해 가장 문자열이 긴 len를 반환해준다.


# 내가 푼 문제 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:

        for i in range(len(s) - 1):
            print(i)
        left = 0
        right = 1
        print(s[left + 1 : right-1])
        #처음부터 문자열을 뒤집어봐서 전체문자열이 이미 팰린드롬인지를 확인
        if len(s)<2 or s==s[::-1]:
            return s
        #print(reversed(s)) #<reversed object at 0x10186ff10>
        # 리스트형식으로 출력되는 sorted와는 다르게 출력조차 되지않는다.
        # 팰린드롬 문자열을 넣는 리스트
        str_list = []
        #홀수개의 문자열을 확인하는 포인터
        for i in range(0, len(s)-2):
            for j in range(0, len(s)//2):
                if i - j >= 0:
                    if ( s[i-j:i+j+3] == ''.join(reversed(s[i-j:i+j+3])) ) :
                        str_list.append(s[i - j:i + j + 3])
                    else:
                        break
                else:
                    break
        # 짝수개의 문자열을 확인하는 포인터
        for i in range(0, len(s)-1):
            for j in range(0, len(s)//2):
                if i - j >= 0:
                    if ( s[i-j:i+j+2] == ''.join(reversed(s[i-j:i+j+2])) ) :
                        str_list.append(s[i - j:i + j + 2])
                    else:
                        break
                else:
                    break
        # 팰린드롬 리스트에 아무것도 없을 시 첫번째 원소값을 리턴
        return max(str_list, key=len, default=s[0])


# 책에서 나온 문제풀이
# 책에서 나온 문제풀이는 테스트케이스에서 s = "ac" 인경우에 "a"를 반환해야하는데
# "c"를 반환한다.
# 문제 오류라고 생각한다.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result
'''
a = Solution()
print(a.longestPalindrome("2351231"))
