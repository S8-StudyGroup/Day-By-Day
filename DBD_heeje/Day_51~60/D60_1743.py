# [BOJ] 1743. 음식물 피하기
# 실행 시간 : 72 ms
# 메모리 : 34068 KB

from collections import deque
import sys
input = sys.stdin.readline

def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True
    cnt = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx]:
                visited[ny][nx] = True
                cnt += 1
                queue.append((ny, nx))

    return cnt

N, M, K = map(int, input().split())
matrix = [[False] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
answer = 0

for _ in range(K):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = True

for i in range(N):
    for j in range(M):
        if not visited[i][j] and matrix[i][j]:
            answer = max(answer, bfs(i, j))

print(answer)