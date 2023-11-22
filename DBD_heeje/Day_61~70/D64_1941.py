# [BOJ] 1941. 소문난 칠공주
# 실행 시간 : 236 ms
# 메모리 : 31120 KB


def dfs(princesses, Y_cnt):
    if Y_cnt > 3:
        return
    
    if len(princesses) == 7:
        cand = tuple(sorted([y * 5 + x for y, x in princesses]))
        if cand not in answer_set:
            answer_set.add(cand)
            global answer
            answer += 1
        return
    
    visited[princesses[-1][0]][princesses[-1][1]] = True

    for y, x in princesses:
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                if matrix[ny][nx] == "Y":
                    dfs(princesses + [(ny, nx)], Y_cnt + 1)
                else:
                    dfs(princesses + [(ny, nx)], Y_cnt)

    visited[princesses[-1][0]][princesses[-1][1]] = False

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

matrix = [input() for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
answer = 0
answer_set = set()
for i in range(5):
    for j in range(5):
        if matrix[i][j] == "Y":
            dfs([(i, j)], 1)
        else:
            dfs([(i, j)], 0)
        visited[i][j] = True

print(answer)