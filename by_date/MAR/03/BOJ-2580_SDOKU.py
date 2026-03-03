# BOJ - 2580
# 스도쿠

# 스도쿠 보드가 들어온다.

import sys

N = 9

row_used = [[False] * 10 for _ in range(N)]
col_used = [[False] * 10 for _ in range(N)]
box_used = [[False] * 10 for _ in range(N)]

def box_id(r, c):
    return (r // 3) * 3 + (c // 3)

    pass

zeros = []
board = []
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

# print(col_used)
# print(row_used, col_used, box_used)

def get_cands(r, c):
    b = box_id(r, c)
    res = []
    for num in range(1, 10):
        if not row_used[r][num] and not col_used[c][num] and not box_used[b][num]:
            res.append(num)
    return res

def dfs():
    if not zeros:
        for r in range(9):
            print(*board[r])
        sys.exit(0)

    best_i = -1
    best_cnads = None

    for i, (r, c) in enumerate(zeros):

        cands = get_cands(r, c)

        if not cands:
            return
        
        if best_cnads is None or len(cands) < len(best_cnads):
            best_cnads = cands
            best_i = i
            if len(best_cnads) == 1:
                break

    r, c = zeros.pop(best_i)
    b = box_id(r, c)

    for num in best_cnads:
        board[r][c] = num
        row_used[r][num] = True
        col_used[c][num] = True
        box_used[b][num] = True

        dfs()

        row_used[r][num] = False
        col_used[c][num] = False
        box_used[b][num] = False

    zeros.insert(best_i, (r, c))

dfs()