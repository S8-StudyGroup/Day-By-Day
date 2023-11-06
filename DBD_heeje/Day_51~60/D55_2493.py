# [BOJ] 2493. 탑(PyPy3)
# 소요 시간 : 10 분
# 실행 시간 : 304 ms
# 메모리 : 212324 KB

import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

answer = [0] * N
stack = []

for i in range(N - 1, -1, -1):
    while stack and towers[stack[-1]] < towers[i]:
        answer[stack.pop()] = i + 1
    
    stack.append(i)

print(*answer)