# BOJ - 15683
# 감시

'''
브루트포스 DFS

[STATE]
1. IDX 번째까지 CCTV 방향이 정해진 상태 // 필드

[CHOICE]
1. 각 CCTV의 방향

[CONSTRAINT]
1. 방향은 십자형, 네 방향 뿐이다.
2. 벽은 넘어서 볼 수 없다
3. 다른 CCTV는 넘어서 볼 수 있다.

[CHANGE & ROLLBACK]
1. FIELD

[BASE]
1. idx == len(cctv)

[POURING]
1. 현재 필드의 사각 지대가 최소 크기보다 커지면 실패
2. 그럼 변화가 큰 값부터 계산을 하면 가지치기를 빠르게 할 수 있겠다.
3. CCTV 번호가 큰 IDX 부터 계산하자.
'''

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

cd = [
    0,
    [[0], [1], [2], [3]],
    [(0, 1), (2, 3)],
    [(0, 3), (3, 1), (1, 2), (0, 2)],
    [(0, 2, 3), (0, 3, 1), (3, 1, 2), (1, 2, 0)],
    [(0, 1, 2, 3)]
]

def dfs(idx, count):
    global cctv, max_checked, field
    
    # [BASE]
    if idx == len(cctv):
        max_checked = max(max_checked, count)
        return
    
    # choice, constraint
    r, c, v = cctv[idx]
    
    for i in cd[v]:
        candidates = set()
        for j in i:
            dr, dc = dirs[j]
            nr, nc = r+dr, c+dc

            while 0 <= nr < N and 0 <= nc < M and field[nr][nc] != 6:
                if field[nr][nc] == 0:
                    candidates.add((nr, nc))
                    field[nr][nc] = 7
                nr, nc = nr+dr, nc+dc
            
        dfs(idx+1, count+len(candidates))

        for a, b in candidates:
            field[a][b] = 0


N, M = map(int, input().split())
field = []
cctv = []
zero_count = 0
for r in range(N):
    row = list(map(int, input().split()))
    field.append(row)
    for c in range(M):
        v = row[c]
        if 0 < v < 6:
            cctv.append((r, c, v))
        elif v == 0:
            zero_count += 1 


# 가지치기 위한 방문배열
visited = [[False] * M for _ in range(N)]

cctv.sort(key=lambda x: -x[2])
# print(cctv)

max_checked = float('-inf')
dfs(0, 0)

print(zero_count - max_checked)

