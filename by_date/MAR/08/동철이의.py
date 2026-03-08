# SWEA - 1865 _ 동철이의 일 분배

"""
[1] DFS

[2] 주어진 일이 모두 성공할 확률

[3] RGB 거리랑 같다. DP가 빠르긴 하겠지만 DFS 문제니까 DFS로 풀자.

[4] 파라미터 : 인덱스와 현재 성공 확률

[5] 가지치기 : 의미 없다.
"""

# import sys
# sys.stdin = open('input.txt')

def dfs(idx, possiblity):
    global maxi, N
    # global a

    # 일을 다 하면 끝, 확률 반환
    if idx == N:
        # print(f'{a}번 {possiblity * 100}')
        # a += 1
        maxi = max(maxi, possiblity)
        return
    
    if possiblity <= maxi:
        return
    

    for i in range(N):
        if check_lst[i] == False:
            check_lst[i] = True
            dfs(idx+1, possiblity * (lst[idx][i] / 100))
            check_lst[i] = False



TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    check_lst = [False]*N  # 백트래킹

    # DFS 로 풀어보자
    # a = 1  # 디버깅
    maxi = 0
    dfs(0, 1)

    print(f'#{test_case} {maxi*100:.6f}')