# SWEA - 4881

'''
N-QUEEN 이랑 유사한데 행과 열만 확인하는 문제

[1] 매개변수
    행 인덱스, 열 선택 상태

[2] 선택되지 않은 열 중 하나를 선택하고 다음으로 넘어간다.
    for문을 이용하면 되겠다.
'''

def dfs(idx: int, val: int):
    global N, used_col, board, mini

    if idx == N:
        mini = min(mini, val)
        return 
    
    if val >= mini:
        return
    
    for col in range(N):
        if not used_col[col]:
            used_col[col] = True
            dfs(idx+1, val + board[idx][col])
            used_col[col] = False


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    used_col = [False] * (N+1)

    mini = float('inf')

    dfs(0, 0)

    print(f"#{test_case} {mini}")    