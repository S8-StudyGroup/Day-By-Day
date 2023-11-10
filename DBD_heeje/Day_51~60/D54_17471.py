# [BOJ] 17471. 게리맨더링
# 실행 시간 : 64 ms
# 메모리 : 34096 KB

from collections import deque
import sys
input = sys.stdin.readline

def is_connected(section):
    queue = deque()
    queue.append(section[0])
    v = set(section)
    v.remove(section[0])
    
    while queue:
        s = queue.popleft()

        for w in adj_list[s]:
            if w in v:
                v.remove(w)
                queue.append(w)
    
    return len(v) == 0


N = int(input())
population = list(map(int, input().split()))
adj_list = [[] for _ in range(N + 1)]
visited = set()
min_diff = 1001

for i in range(1, N + 1):
    infos = list(map(int, input().split()))
    adj_list[i].extend(infos[1:])

for i in range(1, 2 ** N - 1):
    if i in visited: continue
    visited.add(i)
    visited.add(2 ** N - 1 - i)
    A, B = [], []
    for j in range(N):
        if (i & (1 << j)):
            A.append(j + 1)
        else:
            B.append(j + 1)
    
    diff = abs(sum([population[a - 1] for a in A]) - sum([population[b - 1] for b in B]))
    if diff >= min_diff: continue
    if is_connected(A) and is_connected(B):
        min_diff = diff

print(min_diff if min_diff != 1001 else -1)