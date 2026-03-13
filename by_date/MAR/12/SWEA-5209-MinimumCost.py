# SWEA - 5209 - MinimumCost

'''
[1] DFS or DP

[2] 행을 하나씩 넘어가며 선택되지 않은 열을 선택

[3] 3 <= N <= 15 | DFS 가능
'''

# 1. DFS
def dfs(row, cur_cost):
    global chart, minimum_cost

    if row == N:
        minimum_cost = min(minimum_cost, cur_cost)
        return
    
    if cur_cost >= minimum_cost:
        return

    for cur in range(N):
        if not used_factory[cur]:
            used_factory[cur] = True
            dfs(row+1, cur_cost + chart[row][cur])
            used_factory[cur] = False


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    chart = [list(map(int, input().split())) for _ in range(N)]
    used_factory = [False] * N

    minimum_cost = 1500

    dfs(0, 0)

    print(f"#{test_case} {minimum_cost}")