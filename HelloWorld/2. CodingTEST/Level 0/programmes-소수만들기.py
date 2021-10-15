def solution(nums):
    answer = 0

    answer_list=list()

    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                answer_list.append(nums[i]+nums[j]+nums[k])
    '''
    from itertools import combinations
    for a in combinations(nums, 3):
        answer_list.append(sum(a))
    '''
    for num in answer_list:
        for i in range(2, (num//2)+1):
            if not num % i:
                break
        else:
            answer += 1
    return answer

