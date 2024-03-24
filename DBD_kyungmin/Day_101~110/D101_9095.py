# [BOJ] 9095. 1, 2, 3 더하기    
# 풀이 시간 : 30 분

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    d = [0] * 12
    d[1], d[2], d[3] = 1, 2, 4

    for i in range(4, N+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
        
    print(d[N])