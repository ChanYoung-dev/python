def GCDofTwoNumbers(a, b):
    while b != 0:
        a, b = b, a%b
    return a


class Solution:
    def solutionA(self, arr):
        GCDarr = arr[0] # 초항
        LCMarr = arr[0] # 초항
        for value in arr[:]:
            print(LCMarr, ",", value, "의 최대공약수 = ", end="")  # 최대공약수 출력
            GCDarr = GCDofTwoNumbers(LCMarr, value)  # GCDarr에 LCMarr과 arr[i]의 최대공약수를 저장
            print(GCDarr)  # GCDarr 출력

            print(LCMarr, ",", value, "의 최소공배수 = ", end="")  # 최소공배수 출력
            LCMarr = LCMarr * value // GCDarr  # LCMarr에 LCMarr과 arr[i]의 최소공배수를 저장
            print(LCMarr)  # LCMarr 출력

a = Solution()
print(a.solutionA([2,6,8,14]))

# https://kimhaksung.tistory.com/entry/python3LCM?category=863211 참조