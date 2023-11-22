# [BOJ] 2110. 공유기 설치
# 실행 시간 : 276 ms
# 메모리 : 38848 KB

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

start = 1
end = houses[-1] - houses[0]

max_dis = end // (C - 1)

while start <= end:
    mid = (start + end) // 2
    if max_dis < mid:
        end = mid - 1
        continue

    cnt = 1
    cur_pos = houses[0]
    for i in range(1, N):
        if houses[i] - cur_pos >= mid:
            cnt += 1
            cur_pos = houses[i]

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)