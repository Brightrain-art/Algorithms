# SWEA - 5208 - ElectroBus

'''
3 <= N <= 100

[1] DFS, 백트래킹

[2] 현재 위치, 현재 배터리 용량, 교체 횟수

[3] 최대한 적게 교체해서 가장 멀리 갈 수 있는 것 찾기

[4] 더 조금 갔는데 교체횟수가 최소를 넘어가면 종료

'''

def dfs(position: int, change_count: int, cur_battery: int):
    global min_change, batteries, N

    if position >= N-1:
        min_change = min(min_change, change_count)
        return

    if change_count > min_change:
        return

    if cur_battery > 0:           
        dfs(position + 1, change_count, cur_battery - 1)

    dfs(position + 1, change_count + 1, batteries[position] - 1)

    # for battery in batteries[position : position + cur_battery]:
    #     used[position + battery] = True
    #     dfs(position + battery, change_count + 1)
    #     used[position + battery] = False


TC = int(input())
for test_case in range(1, TC+1):
    INPUT = list(map(int, input().split()))
    N = INPUT[0]
    batteries = INPUT[1:]
    used = [False] * 2 * N

    min_change = float('inf')

    dfs(0, 0, batteries[0])

    print(f"#{test_case} {min_change}")