# SWEA - 4837 - SumofPart


def dfs(idx: int, value: int):
    global N, K, used, count

    if value > K:
        return
    
    if idx == N+1:
        if value == K:
            count += 1
            return
    
    dfs(idx+1, value)

    if not used[idx]:
        used[idx] = True
        dfs(idx+1, value + idx)
        used[idx] = False

    pass


TC = int(input())
for test_case in range(1, TC+1):
    N, K = map(int, input().split())

    used = [False] * (N+1)
    count = 0

    dfs(1, 0)

    print(count)