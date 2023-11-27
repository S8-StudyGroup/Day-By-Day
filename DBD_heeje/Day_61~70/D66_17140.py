# [BOJ] 17140. 이차원 배열과 연산
# 소요 시간 : 68 ms
# 메모리 : 31120 KB


def A_sort(A):

    flag = False
    if len(A) < len(A[0]):
        flag = True
        copied_A = []
        for i in range(len(A[0])):
            row = []
            for j in range(len(A)):
                row.append(A[j][i])
            copied_A.append(row)
        A = copied_A

    new_A = []
    max_row = 0
    for i in range(len(A)):
        s_dict = dict()
        for j in range(len(A[0])):
            if s_dict.get(A[i][j]):
                s_dict[A[i][j]] += 1
            else:
                s_dict[A[i][j]] = 1
        
        row = []
        for s_tuple in sorted(s_dict.items(), key=lambda x: (x[1], x[0])):
            if s_tuple[0] == 0:
                continue
            row.extend(s_tuple)
        max_row = max(max_row, len(row))
        new_A.append(row)

    for row in new_A:
        while len(row) < max_row:
            row.append(0)
    
    if flag:
        copied_A = []
        for i in range(len(new_A[0])):
            row = []
            for j in range(len(new_A)):
                row.append(new_A[j][i])
            copied_A.append(row)
        new_A = copied_A
    return new_A

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

for time in range(101):
    if r - 1 < len(A) and c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        print(time)
        break

    A = A_sort(A)

else:
    print(-1)