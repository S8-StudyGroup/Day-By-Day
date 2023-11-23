# [BOJ] 29703. 펭귄의 하루(PyPy3)
# 실행 시간 : 1388 ms
# 메모리 : 256364 KB

from collections import deque
import sys
input = sys.stdin.readline



def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx, 0, 0))
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]
    visited[sy][sx][0] = True

    while queue:
        y, x, cnt, is_hunted = queue.popleft()

        if is_hunted == 1 and y == home_y and x == home_x:
            return cnt

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if in_range(ny, nx) and not visited[ny][nx][is_hunted] and (pg_map[ny][nx] == "E" or pg_map[ny][nx] == "F"):
                if is_hunted == 0 and pg_map[ny][nx] == "F":
                    visited[ny][nx][1] = True
                    queue.append((ny, nx, cnt + 1, 1))
                else:
                    visited[ny][nx][is_hunted] = True
                    queue.append((ny, nx, cnt + 1, is_hunted))

    return -1


direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
N, M = map(int, input().split())
pg_map = []
start_y, start_x = 0, 0
fish_y, fish_x = 0, 0
home_y, home_x = 0, 0
for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == "S":
            start_y, start_x = i, j
            row[j] = "E"
        elif row[j] == "H":
            home_y, home_x = i, j
            row[j] = "E"
    pg_map.append(row)

print(bfs(start_y, start_x))