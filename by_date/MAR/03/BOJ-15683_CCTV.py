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
    [0, 1, 2, 3],
    [(0, 1), (2, 3)],
    [(0, 3), (3, 1), (1, 2), (0, 2)],
    [(0, 2, 3), (0, 3, 1), (3, 1, 2), (1, 2, 0)]
    [(0, 1, 2, 3)]
]

def sight_check(r, c, v):
    global candidates
    # 방향설정부터
    if v == 1:
        for i in cd[v]:
            dr, dc = dirs[i]
            nr, nc = r+dr, c+dc

            while 0 <= nr < N and 0 <= nc < M and field[nr][nc] != 6:

                if field[nr][nc] == 0:

                    candidates.add((nr, nc))
                
                nr, nc = nr+dr, nc+dc


    pass

def dfs(idx):
    global cctv
    
    # [BASE]
    # if idx == len(cctv):
    #     # 사각지대 계산 // 변수 필요
    #     bs = 0
    #     for row in field:
    #         bs += row.count(0)
    #     min_blind_sector = min(min_blind_sector, bs)
    #     return

    if idx == len(cctv):
        return

    # choice, constraint
    r, c, v = cctv[idx]
    cd[v] == "cctv 번호"
    # 번호에 따라 보는 방향이 다르다.
    # 함수로 빼야 깔끔할 것 같다.
    for i in cd[v]:
        dr, dc = dirs[i]
        nr, nc = r+dr, c+dc

        candidates = set()

        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if field[nr][nc] == 6:
            continue

        while not (0 <= nr < N and 0 <= nc < M) and field[nr][nc] != 6:        
            # 필드를 직접 바꿀 필요는 없다.
            # 좌표 리스트를 만들어서 관리하는게 낫겠다.
            candidates.add((nr, nc))
            nr, nc = nr+dr, nc+dc

    dfs(idx + 1)


    pass

N, M = map(int, input().split())
field = []
cctv = []
for r in range(N):
    row = list(map(int, input().split()))
    field.append(row)
    for c in range(N):
        v = row[c]
        if 0 < v < 6:
            cctv.append((r, c, v))

# 가지치기 위한 방문배열
visited = [[False] * M for _ in range(N)]

cctv.sort(key=lambda x: -x[2])
# print(cctv)

min_blind_sector = float('inf')
candidates = set()