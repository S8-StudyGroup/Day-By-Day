# [BOJ] 1043. 거짓말
# 실행 시간 : 68 ms
# 메모리 : 34068 KB

from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline 


N, M = map(int, input().split())
truth_list = list(map(int, input().split()))[1:]
can_tell_lie = [True] * (N + 1)
answer = 0
    
visited = set()
adj_list = [[] for _ in range(N + 1)]
party_list = []
for i in range(M):
    party = list(map(int, input().split()))[1:]
    for a, b in permutations(party, 2):
        if (a, b) not in visited:
            visited.add((a, b))
            adj_list[a].append(b)

    party_list.append(party)

for truth in truth_list:
    if not can_tell_lie[truth]: continue
    can_tell_lie[truth] = False
    queue = deque()
    queue.append(truth)
    
    while queue:
        truth_person = queue.popleft()

        for relationship in adj_list[truth_person]:
            if can_tell_lie[relationship]:
                can_tell_lie[relationship] = False
                queue.append(relationship)

for party in party_list:
    for person in party:
        if not can_tell_lie[person]:
            break
    else:
        answer += 1

print(answer)
