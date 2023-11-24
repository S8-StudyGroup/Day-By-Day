# [Programmers] 17298. 오큰수
# 실행 시간 : 00 ms
# 메모리 : 00 KB

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
stack = []
answer = [-1] * N

for i in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

sys.stdout.write(*answer)