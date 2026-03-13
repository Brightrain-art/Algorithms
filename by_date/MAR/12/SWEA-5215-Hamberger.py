# SWEA - 5215 - Hamberger


def dfs(cur_score: int, idx: int, cur_cal: int):
    global N, L, ingredient, maximum_score

    if cur_cal > L:
        return
    
    if idx == N:
        maximum_score = max(maximum_score, cur_score)
        return
    
    if not used[idx]:
        used[idx] = True
        dfs(cur_score + ingredient[idx][0], idx + 1, cur_cal + ingredient[idx][1])
        used[idx] = False

    dfs(cur_score, idx+1, cur_cal)

    pass


TC = int(input())
for test_case in range(1, TC+1):
    N, L = map(int, input().split())
    ingredient = [tuple(map(int, input().split())) for _ in range(N)]
    used = [False] * N

    maximum_score = 0
    dfs(0, 0, 0)

    print(f"#{test_case} {maximum_score}")