# [BOJ] 2240. 자두나무
# 실행 시간 : 52 ms
# 메모리 : 31120 KB

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
targets = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]
if targets[0] == 1:
    dp[1][0] = 1

for i in range(1, T + 1):
    for j in range(W + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # 1번 나무고 1번에 서있거나 2번 나무고 2번에 서있을 때
        if targets[i] - 1 == j % 2:
            dp[i][j] += 1

print(dp[-1][-1])