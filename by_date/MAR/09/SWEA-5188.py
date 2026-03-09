# SWEA - 5188 - 최소합
import sys
sys.stdin = open('input.txt')

dirs = [
    (1, 0), (0, 1)
]

def dfs(r, c, val):
    global N, board, min_val

    if (r, c) == (N-1, N-1):
        min_val = min(min_val, val)
        return
    
    if val > min_val:
        return

    for dr, dc in dirs:
        nr, nc = r+dr, c+dc

        if 0 <= nr < N and 0 <= nc < N \
            and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, val + board[nr][nc])
            visited[nr][nc] = False



TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True

    min_val = float('inf')
    dfs(0, 0, board[0][0])

    print(f'#{test_case} {min_val}')
    # print(bfs(0, 0, board[0][0]))