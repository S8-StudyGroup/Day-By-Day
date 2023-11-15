# [BOJ] 1863. 스카이라인 쉬운거
# 실행 시간 : 56 ms
# 메모리 : 31120 KB

import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
         
    if (not stack and y != 0) or (stack and stack[-1] < y):
        stack.append(y)
        answer += 1
    
print(answer)