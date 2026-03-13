# SWEA - 5656 - BreackBrick

'''
[1] BFS

[2] 남은 횟수, 현재 블럭 상태

[3] N번 진행했을 때 남은 벽돌의 최소 개수

재귀 필요?

1. 블럭을 떨어뜨리고
2. 터트리고
3. 연쇄작용도 계산해서 다 터트리고
4. 중력작용
'''

from collections import deque
import copy

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def can_move(r, c, cur_status):
    global W, H

    if not (0 <= r < H and 0 <= c < W):
        return False
    return True


def break_brick(col: int, cur_status: list):

    breaked_brick = 0
    # col 에서 가장 위의 블럭을 찾는다.
    for row in range(H):
        if cur_status[row][col] != 0:
            power = cur_status[row][col]
            # 1인 블록이면 부수고 끝
            if power == 1:
                cur_status[row][col] = 0
                breaked_brick += 1
                return breaked_brick, cur_status
            else:
                cur_status[row][col] = 0
                q = deque([(row, col, power)])

                # 연쇄작용까지 계산
                while q:
                    r, c, p = q.popleft()

                    for dr, dc in dirs:
                        pr, pc = r, c

                        while p > 1:
                            nr, nc = pr+dr, pc+dc

                            if can_move(nr, nc, cur_status):
                                breaked_brick += 1
                                p -= 1
                                p = max(p, cur_status[r][c])
                                cur_status[nr][nc] = 0

                                q.append((nr, nc, p))

                                pr, pc = nr, nc

                            else:
                                break
                        
                return breaked_brick, cur_status
    return breaked_brick, cur_status
    


def gravity(cur_status):
    global W, H

    # 행 리스트로 만들고
    # 0 다 지우고
    # 0 다 채우고
    # 다시 집어넣고
    for col in range(W):
        col_lst = []

        for row in range(H):
            if cur_status[row][col] != 0:
                col_lst.append(cur_status[row][col])
            
        while len(col_lst) < H:
            col_lst.insert(0, 0)
        
        for row in range(H):
            cur_status[row][col] = col_lst.pop(0)

    # print(cur_status)
    return cur_status


def dfs(opportunity: int, remain_brick: int, cur_status: list):
    global N, W, H, minimum_brick

    # [Base] opportunity == N
    if opportunity == N:
        minimum_brick = min(minimum_brick, remain_brick)
        return

    for col in range(W):
        # col 에 떨어뜨려서 계산하고 // 중력작용
        status = copy.deepcopy(cur_status)
        breaked_brick, cur_status = break_brick(col, cur_status)
        cur_status = gravity(cur_status)

        dfs(opportunity + 1, remain_brick - breaked_brick, cur_status)

        cur_status = copy.deepcopy(status)

TC = int(input())
for test_case in range(1, TC+1):
    N, W, H = map(int, input().split())
    status = []
    remain_brick = 0
    for r in range(H):
        row = list(map(int, input().split()))
        status.append(row)
        for c in range(W):
            if row[c] != 0:
                remain_brick += 1
    print(remain_brick)

    # cleared = [[False] * W for _ in range(H)]
    minimum_brick = 180

    dfs(0, remain_brick, status)

    print(minimum_brick)