class Solution:
    def solutionA(self, numbers, hand):
        result = ""
        left, right = [4, 1], [4, 3]
        num_map = [[4, 2], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
        for number in numbers:
            print("비교할 숫자", number, num_map[number])
            print("변환 전 : left : {0}, right : {1}" .format(left, right))
            if number % 3 == 1:
                result += "L"
                left = num_map[number]
                print("left 이동: ", left)
            elif number % 3 == 0 and number != 0:
                result += "R"
                right = num_map[number]
                print("right 이동: ", right)
            else:
                if abs(num_map[number][0] - left[0]) + abs(num_map[number][1] - left[1]) < abs(num_map[number][0] - right[0]) + abs(num_map[number][1] - right[1]):
                    result += "L"
                    left = num_map[number]
                elif abs(num_map[number][0] - left[0]) + abs(num_map[number][1] - left[1]) > abs(num_map[number][0] - right[0]) + abs(num_map[number][1] - right[1]):
                    result += "R"
                    right = num_map[number]
                else:
                    print("서로 거리가 같습니다")
                    if hand == "left":
                        result += "L"
                        left = num_map[number]
                    else:
                        result += "R"
                        right = num_map[number]

            print("변환 후 :left : {0}, right : {1}" .format(left, right))
            print("---------------------------")
        print(result)
        return result


a = Solution()
print(a.solutionA([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))