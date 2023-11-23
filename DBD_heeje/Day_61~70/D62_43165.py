# [Programmers] 43165. 타겟 넘버

def solution(numbers, target):
    N = len(numbers)
    answer = 0
    for i in range(2 ** N):
        sum_value = 0
        for j in range(N):
            if i & (1 << j):
                sum_value += numbers[j]
            else:
                sum_value -= numbers[j]
        if sum_value == target:
            answer += 1
    return answer