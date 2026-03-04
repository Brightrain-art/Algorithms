# SWEA - 1226
# 미로1

import sys
from collections import deque
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(r, c, er, ec):
    global done

    q = deque([(r, c)])
    visited = [[False]*16 for _ in range(16)]
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        if (r, c) == (er, ec):
            done = True
            return

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if not (0 <= nr < 16 and 0 <= nc <16):
                continue

            if maze[nr][nc] == 1:
                continue

            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            q.append((nr, nc))


    pass

for _ in range(1, 11):
    test_case = int(input())
    maze = []
    for r in range(16):
        row = list(map(int, list(input())))
        maze.append(row)
        for c in range(16):
            if row[c] == 2:
                sr, sc = r, c
            elif row[c] == 3:
                er, ec = r, c
    
    done = False
    bfs(sr, sc, er, ec)

    print(f'#{test_case} {1 if done else 0}')