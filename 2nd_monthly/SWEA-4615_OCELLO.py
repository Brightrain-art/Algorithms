# SWEA - 4615
# 재미있는 오셀로 게임

'''
오셀로 게임
1. 흑과 백이 번갈아가며 돌을 둔다
2. 돌을 뒀을 때 같은 색 돌 사이의 돌은 반대 색으로 변한다.
3. 고립된 돌은 존재하지 않는다.
4. 상대의 돌을 공격할 수 없다면 돌을 둘 수 없다
5. 돌을 둘 수 없다면 다음 플레이어에게 턴이 넘어간다.
6. 보드의 크기와 초기 상태가 주어질 때 게임이 끝난 후 각 돌의 수를 출력해라.
'''

import sys
sys.stdin = open('input.txt')

from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

rev = [0, 2, 1]

def gogo(r, c, color):

    if not (0 <= r < N and 0 <= c < N):
        return False
    if board[r][c] != rev[color]:
        return False
    # if board[r][c] == 0:
    #     return False
    # if board[r][c] == color:
    #     return False
    return True

def change(r, c, dr, dc, color):
    global board

    cand = []
    while True:

        nr, nc = r+dr, c+dc
        # if not gogo(nr, nc, color):
        #     break
        if not (0 <= nr < N and 0 <= nc < N):
            break

        if board[nr][nc] == 0:
            break

        if board[nr][nc] == color:
            for cr, cc in cand:
                board[cr][cc] = color
            break

        if board[nr][nc] == rev[color]:
            cand.append((nr, nc))
            r, c = nr, nc


TC = int(input())
for test_case in range(1, TC+1):
    # N : 보드 크기, M : 플레이어의 턴 수
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]  # 기록 할 배열
    cen = N//2  # center
    board[cen][cen] = board[cen-1][cen-1] = 2  # 1: 흑돌, 2: 백돌
    board[cen-1][cen] = board[cen][cen-1] = 1

    # 입력에 좌표와 색이 주어진다. (r, c, color)
    # 받으면서 한 번에 처리하자.
    # 함수 필요

    for _ in range(M):
        r, c, color = map(int, input().split())
        r, c = r-1, c-1
        board[r][c] = color

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if gogo(nr, nc, color):
                change(r, c, dr, dc, color)

    black = 0
    white = 0

    for row in board:
        black += row.count(1)
        white += row.count(2)
    
    print(f'#{test_case} {black} {white}')