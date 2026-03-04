# BOJ - 2580
# 스도쿠

'''
[1] STATE
몇 번 IDX 까지 채웠는지. ( 빈 칸 현황 )

[2] CHOICE
빈 칸에 어떤 숫자를 넣을 지

[3] CONSTRAINT
스도쿠 규칙 ( 행, 열, 박스에 같은 숫자가 없도록 )

[4] CHANGE, ROLLBACK
빈 칸에 넣은 숫자

[5] BASE CASE
인덱스가 끝까지 갔거나
더 넣을 수 있는 숫자가 없을 때 종료
'''
'''
1. 빈 칸을 찾는다.
2. 빈 칸을 순회하며 후보군을 찾는다.
3. 각 칸의 후보군을 한 개씩 넣어본다.
4. 후보군이 없는 칸이 생기면 종료 ( 실패 )
5. 끝까지 문제없이 들어가면 ( 성공 )

- 후보군이 적은 칸 부터 하나씩 넣어보면 더 빨리 끝나겠다.
- 빈 칸을 찾으면서 후보군을 찾을 수 있나?
'''

import sys

N = 9
row_used = [[False] * 10 for _ in range(N)]
col_used = [[False] * 10 for _ in range(N)]
box_used = [[False] * 10 for _ in range(N)]

def box_id(r, c):
    return (r//3)*3 + (c//3)


board = []
zeros = []
for r in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for c in range(N):
        v = row[c]
        if v == 0:
            zeros.append((r, c))
        else:
            row_used[r][v] = True
            col_used[c][v] = True
            box_used[box_id(r, c)][v] = True


def candidates(idx):
    r, c = zeros[idx]

    b = box_id(r, c)
    cand = []
    for v in range(1, 10):
        if not row_used[r][v] and not col_used[c][v] and not box_used[b][v]:
            cand.append(v)
    return cand

def dfs(idx):


    if idx == len(zeros):
        for i in range(9):
            print(*board[i])
        sys.exit(0)
        

    # cand = []
    # for i, (r, c) in enumerate(zeros):
    #     cand.append((i, candidates(r, c)))
    # cand.sort(key=lambda x: -len(x[1]))

    # best_idx = cand[0][0]
    # best_cand = 

    r, c = zeros[idx]
    cand = candidates(idx)
    if len(cand) == 0:
        return

    b = box_id(r, c)
    for num in cand:
        board[r][c] = num
        row_used[r][num] = True
        col_used[c][num] = True
        box_used[b][num] = True

        dfs(idx+1)

        row_used[r][num] = False
        col_used[c][num] = False
        box_used[b][num] = False

        board[r][c] = 0
        

    pass

dfs(0)