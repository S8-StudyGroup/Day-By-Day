# [BOJ] 11053. 가장 긴 증가하는 부분 수열
# 실행 시간 : 160 ms
# 메모리 : 31120 KB

N = int(input())
numbers = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))